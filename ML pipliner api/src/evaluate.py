# src/evaluate.py
from joblib import load
import pandas as pd
from sklearn.metrics import classification_report
from pipeline import load_data

model = load("churn_pipeline.pkl")
df = load_data("WA_Fn-UseC_-Telco-Customer-Churn.csv")
X = df.drop("Churn", axis=1)
y = df["Churn"].map({'Yes': 1, 'No': 0})

y_pred = model.predict(X)
print(classification_report(y, y_pred))
