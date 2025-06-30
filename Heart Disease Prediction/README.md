Heart Disease Prediction Web App
A Flask-based web application that predicts whether a patient is at risk of heart disease based on their health data.
This project applies machine learning classification models on a cleaned Heart Disease UCI dataset with a user-friendly interactive web interface.

Task Objective
Build a heart disease prediction system using supervised machine learning.

Allow users to input patient health details via a web form.

Train models to predict heart disease presence (Yes/No).

Provide model evaluation results and visualizations (like feature importance charts).

Dataset Used
Dataset: Heart Disease UCI Dataset

Source: Kaggle - Heart Disease UCI Dataset

Features Used:

Age

Sex

Chest Pain Type (cp)

Resting Blood Pressure (trestbps)

Cholesterol (chol)

Fasting Blood Sugar (fbs)

Resting ECG Results (restecg)

Maximum Heart Rate (thalach)

Exercise Induced Angina (exang)

ST Depression (oldpeak)

Slope of ST segment (slope)

Number of major vessels (ca)

Thalassemia (thal)

Target Variable:

Presence of Heart Disease (Binary classification: 1 = Disease, 0 = No Disease)

Models Applied
Logistic Regression

Decision Tree Classifier

Both models are implemented using scikit-learn (sklearn).

Features & Workflow
Web App Flow:
User Input:

Web form collects patient health details (age, cholesterol, blood pressure, etc).

Model Prediction:

User submits form → Data fed into ML model → Returns heart disease prediction.

Model Evaluation:

Accuracy, Confusion Matrix, and Feature Importance calculated and shown.

Visualization:

Bar chart showing top important features influencing the prediction.

Styling:

Responsive, colorful frontend with improved CSS.

Key Results and Findings
Metric Logistic Regression Decision Tree
Accuracy (on Test Set) ~82% ~79%
Best Features Cholesterol, Age, Max Heart Rate, ST Depression Similar but decision tree more flexible
Observations Logistic Regression gives stable results, Decision Tree captures non-linearities

Technologies Used
Python

Flask

scikit-learn

pandas

numpy

matplotlib / seaborn

HTML5 / CSS3 (with styling for better user experience)