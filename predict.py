import joblib
import pandas as pd
import numpy as np
from sklearn.feature_extraction import DictVectorizer

# =============================
# LOAD ARTIFACTS
# =============================

def load_artifacts():
    model = joblib.load("model.joblib")
    dv = joblib.load("dictvectorizer.joblib")
    return model, dv

# =============================
# PREDICTION FUNCTION
# =============================

def predict(sample: dict):
    """
    sample: dictionary with required categorical fields
    returns: prediction + probability
    """
    model, dv = load_artifacts()

    # Convert to vector
    X = dv.transform([sample])

    pred = model.predict(X)[0]
    prob = model.predict_proba(X)[0][1]

    return {
        "adopted": int(pred),
        "probability": float(prob)
    }

# =============================
# MAIN (TEST SAMPLE)
# =============================
if __name__ == "__main__":
    example = {
        "intake_type": "Stray",
        "intake_condition": "Normal",
        "animal_type": "Dog",
        "sex_upon_intake": "Neutered Male",
        "breed": "Labrador Retriever Mix",
        "color": "Black",
        "month": 5,
        "year": 2020
    }

    result = predict(example)
    print("Prediction:", result)