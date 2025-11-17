# =============================
# 1. PACKAGES
# =============================
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer
from sklearn.metrics import f1_score
from sklearn.ensemble import RandomForestClassifier
import joblib

# =============================
# 2. DATA PREPARATION
# =============================
INTAKES_URL = "https://data.austintexas.gov/api/views/wter-evkm/rows.csv?accessType=DOWNLOAD"
OUTCOMES_URL = "https://data.austintexas.gov/api/views/9t4d-g238/rows.csv?accessType=DOWNLOAD"

def load_and_prepare_data():
    df_intakes = pd.read_csv(INTAKES_URL)
    df_outcomes = pd.read_csv(OUTCOMES_URL)

    # Normalize column names
    df_intakes.columns = df_intakes.columns.str.lower().str.replace(" ", "_")
    df_outcomes.columns = df_outcomes.columns.str.lower().str.replace(" ", "_")

    # Keep only useful outcome columns
    df_outcomes = df_outcomes[["animal_id", "datetime", "outcome_type"]]

    # Merge datasets
    df = pd.merge(df_intakes, df_outcomes, on="animal_id", how="inner", suffixes=("_intake", "_outcome"))

    # Target variable
    df["adopted"] = (df["outcome_type"] == "Adoption").astype(int)

    # Fill missing categorical values
    df = df.fillna({
        "intake_type": "Unknown",
        "intake_condition": "Unknown",
        "sex_upon_intake": "Unknown",
        "monthyear": "Unknown"
    })

    # Convert monthyear to month/year
    df["monthyear"] = pd.to_datetime(df["monthyear"], errors="coerce")
    df["month"] = df["monthyear"].dt.month.fillna(0).astype(int)
    df["year"] = df["monthyear"].dt.year.fillna(0).astype(int)

    return df

# =============================
# 3. VECTORIZATION
# =============================

def vectorize(df):
    categorical = ["intake_type", "intake_condition", "animal_type", "sex_upon_intake", "breed", "color"]
    numeric = ["month", "year"]

    dv = DictVectorizer(sparse=False)
    dicts = df[categorical].to_dict(orient="records")
    X_cat = dv.fit_transform(dicts)

    X_num = df[numeric].values
    X = np.hstack([X_num, X_cat])

    y = df["adopted"].values
    return X, y, dv

# =============================
# 4. MODEL TRAINING
# =============================

def train_model(X_train, y_train):
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    return model

# =============================
# 5. EVALUATION
# =============================

def evaluate(model, X_test, y_test):
    y_pred = model.predict(X_test)
    return f1_score(y_test, y_pred)

# =============================
# 6. MODEL SAVING
# =============================

def save_artifacts(model, dv):
    import os
    os.makedirs("models", exist_ok=True)
    joblib.dump(model, "models/model.joblib")
    joblib.dump(dv, "models/dv.joblib")
    print("Saved model and DictVectorizer in models/ folder.")
    # joblib.dump(model, "model.joblib")
    # joblib.dump(dv, "dictvectorizer.joblib")
    # print("Saved: model.joblib, dictvectorizer.joblib")

# =============================
# MAIN EXECUTION
# =============================
if __name__ == "__main__":
    print("Loading data...")
    df = load_and_prepare_data()

    print("Vectorizing...")
    X, y, dv = vectorize(df)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    print("Training model...")
    model = train_model(X_train, y_train)

    print("Evaluating...")
    score = evaluate(model, X_test, y_test)
    print(f"F1-score: {score:.4f}")

    print("Saving artifacts...")
    save_artifacts(model, dv)

    print("Training complete!")
