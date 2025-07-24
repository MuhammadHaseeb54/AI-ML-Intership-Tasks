# src/predict.py
from joblib import load
import pandas as pd

model = load("churn_pipeline.pkl")

def predict_single(sample: dict):
    df = pd.DataFrame([sample])
    return model.predict(df)[0], model.predict_proba(df)[0].max()
