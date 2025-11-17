from fastapi import FastAPI, HTTPException, Request
import joblib
import os

# ---------------------------
# Load model and DictVectorizer
# ---------------------------

# Get the project root directory (two levels up from src/)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "models", "model.joblib")
DV_PATH = os.path.join(BASE_DIR, "models", "dictvectorizer.joblib")

# Load artifacts
try:
    model = joblib.load(MODEL_PATH)
    dv = joblib.load(DV_PATH)
except FileNotFoundError as e:
    raise RuntimeError(f"Model or DictVectorizer not found: {e}")

# ---------------------------
# FastAPI app
# ---------------------------
app = FastAPI(title="Pet Adoption Prediction API")

@app.post("/predict")
async def predict(request: Request):
    data = await request.json()
    if not data:
        raise HTTPException(status_code=400, detail="No input data provided")
    
    try:
        X = dv.transform([data])
        pred = model.predict(X)[0]
        prob = model.predict_proba(X)[0][1]
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    return {"adopted": int(pred), "probability": float(prob)}

@app.get("/health")
def health():
    return {"status": "ok"}
