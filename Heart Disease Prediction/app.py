from flask import Flask, render_template, request
import numpy as np
import joblib

app = Flask(__name__)
# Load the saved model
model = joblib.load('heart_disease_model.pkl')
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            # Get user input from form
            age = float(request.form['age'])
            sex = float(request.form['sex'])
            cp = float(request.form['cp'])
            trestbps = float(request.form['trestbps'])
            chol = float(request.form['chol'])
            fbs = float(request.form['fbs'])
            restecg = float(request.form['restecg'])
            thalach = float(request.form['thalach'])
            exang = float(request.form['exang'])
            oldpeak = float(request.form['oldpeak'])
            slope = float(request.form['slope'])
            ca = float(request.form['ca'])
            thal = float(request.form['thal'])

            # Prepare input for model
            input_features = np.array([[age, sex, cp, trestbps, chol, fbs, restecg, 
                                        thalach, exang, oldpeak, slope, ca, thal]])
            # Make prediction
            prediction = model.predict(input_features)[0]
            result = "High Risk of Heart Disease" if prediction == 1 else "Low Risk (No Heart Disease)"
            return render_template('result.html', result=result)
        except Exception as e:
            return f"Error: {e}"

if __name__ == '__main__':
    app.run(debug=True)
