from flask import Flask, render_template, request
from joblib import load
import pandas as pd

app = Flask(__name__)

# Load the trained pipeline
model = load("churn_pipeline.pkl")

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    confidence = None

    if request.method == "POST":
        # Collect form data
        form = request.form

        # Create DataFrame with a single row
        sample = pd.DataFrame([{
            "gender": form["gender"],
            "SeniorCitizen": int(form["SeniorCitizen"]),
            "Partner": form["Partner"],
            "Dependents": form["Dependents"],
            "tenure": float(form["tenure"]),
            "MonthlyCharges": float(form["MonthlyCharges"]),
            "TotalCharges": float(form["TotalCharges"]),
            "PhoneService": "Yes",              # optional fields if needed
            "MultipleLines": "No",
            "InternetService": "Fiber optic",
            "OnlineSecurity": "No",
            "OnlineBackup": "Yes",
            "DeviceProtection": "No",
            "TechSupport": "No",
            "StreamingTV": "No",
            "StreamingMovies": "Yes",
            "Contract": form["Contract"],
            "PaperlessBilling": form["PaperlessBilling"],
            "PaymentMethod": form["PaymentMethod"]
        }])

        # Make prediction
        pred_label = model.predict(sample)[0]
        pred_proba = model.predict_proba(sample)[0].max()

        prediction = "Yes" if pred_label == 1 else "No"
        confidence = round(pred_proba * 100, 2)

    return render_template("index.html", prediction=prediction, confidence=confidence)

if __name__ == "__main__":
    app.run(debug=True)
