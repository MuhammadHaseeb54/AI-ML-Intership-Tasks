# AI-ML-Intership-Tasks

# Task 01

# Iris Dataset Exploration and Visualization

##  Task Objective

The goal of this task is to **explore and visualize the Iris dataset** using Python libraries such as `pandas`, `seaborn`, and `matplotlib`. This task emphasizes data understanding through descriptive statistics and visual interpretation, rather than machine learning.

##  Dataset Used

- **Dataset**: Iris Dataset  
- **Source**: Built-in dataset available via the `seaborn` library or as a CSV file  
- **Description**: The dataset contains 150 records of iris flowers with 4 numeric features (sepal length, sepal width, petal length, petal width) and a target label (species).

##  Models Applied

**No machine learning models** were applied in this task.  
The focus is on **exploratory data analysis (EDA)** and basic data visualization.

## Key Results and Findings

- **Data Overview**:
  - Dataset shape: `(150, 5)`
  - No missing values found.
  - Three distinct species: `setosa`, `versicolor`, `virginica`.

- **Visualizations**:
  - **Scatter plots** revealed clear feature separation, especially between petal dimensions.
  - **Histograms** showed normal distribution for most features, with some skewness.
  - **Box plots** helped detect mild outliers, especially in `sepal width`.

- **Insights**:
  - Petal length and width are the most discriminative features for classifying species.
  - `Setosa` species are distinctly separated from the other two.

##  Files

- `Iris_notebook.ipynb` – Jupyter notebook containing all the code, visualizations, and analysis.

## Skills Practiced

- Data loading and inspection using `pandas`
- Summary statistics and data exploration
- Visual analysis using `matplotlib` and `seaborn`

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

**Task 02**

**📈 Stock Price Prediction Web App (Short-Term Forecasting)**

- A Flask-based web application that uses historical stock market data from Yahoo Finance to predict the next day's closing price for any given stock ticker (e.g., Apple, Tesla).
This project demonstrates time series handling, regression modeling, and data visualization.

**Task Objective**
- Build a machine learning model to predict the next day's closing stock price based on historical data.
- Allow users to select stock ticker symbols (like AAPL, TSLA, GOOGL) and choose between Linear Regression and Random Forest models.
- Provide an interactive web interface for input and result visualization.
- Display Actual vs Predicted stock prices for test data.

**Dataset Used**
Source: Yahoo Finance
Library Used for Data Retrieval: yfinance
Data Fields Used:
- Open
- High
- Low
- Volume
- Close (as target: next day’s close)

**Features and Workflow**
**User Input:**
- Stock ticker symbol (e.g., AAPL, MSFT, TSLA)
- Model choice (Linear Regression or Random Forest)
**Backend Processing:**
- Downloads historical stock data from Yahoo Finance
- Prepares dataset (time-series target shifting)
- Trains selected regression model
- Makes predictions
- Calculates R² Score
**Visualization:**
- Plots Actual vs Predicted Closing Prices
- Displays model accuracy (R²)

**Error Handling:**
-- Invalid ticker input error
-- Data unavailability error (if Yahoo Finance has no data)
**Front-End Design:**
-- Colorful, animated, responsive UI
-- Gradient backgrounds, glassmorphism, glowing buttons
-- Error messages styled in soft red overlays

**Models Applied**
- Linear Regression
- Random Forest Regressor
Both models are implemented using scikit-learn.

**Key Results and Findings**
**Metric**	**Result**
**Prediction Goal**	Next day's closing price
**Evaluation Metric**	R² Score
- Visualization	Actual vs Predicted Close Price Graph
**Test Results**
- Models typically achieved R² Scores ranging between 0.6 - 0.9 depending on stock and time period. Random Forest often performed better on noisy stocks.
- Finding	Including features like Open, High, Low, and Volume helps in capturing stock movement patterns for short-term prediction. However, stock market data is inherently noisy, so model performance varies per stock.

**Screenshots**
![image](https://github.com/user-attachments/assets/8371fc0f-e0b1-4eb8-944b-af72ed2638bc)
![image](https://github.com/user-attachments/assets/82e4f02f-2507-440f-bd3d-ef73077369b2)



**Technologies Used**
- Python
- Flask
- yfinance
- pandas
- numpy
- scikit-learn
- matplotlib
- HTML5 / CSS3 (Responsive, Gradient, Animated)
  
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

**Task 03**

**Heart Disease Prediction Web App**

A Flask-based web application that predicts whether a patient is at risk of heart disease based on their health data.
This project applies machine learning classification models on a cleaned Heart Disease UCI dataset with a user-friendly interactive web interface.

**Task Objective**
- Build a heart disease prediction system using supervised machine learning.
- Allow users to input patient health details via a web form.
- Train models to predict heart disease presence (Yes/No).
- Provide model evaluation results and visualizations (like feature importance charts).

**Dataset Used**
- Dataset: Heart Disease UCI Dataset
- Source: Kaggle - Heart Disease UCI Dataset

**Features Used:**
- Age
- Sex
- Chest Pain Type (cp)
- Resting Blood Pressure (trestbps)
- Cholesterol (chol)
- Fasting Blood Sugar (fbs)
- Resting ECG Results (restecg)
- Maximum Heart Rate (thalach)
- Exercise Induced Angina (exang)
- ST Depression (oldpeak)
- Slope of ST segment (slope)
- Number of major vessels (ca)
- Thalassemia (thal)
**Target Variable:**
 Presence of Heart Disease (Binary classification: 1 = Disease, 0 = No Disease)

**Models Applied**
- Logistic Regression
- Decision Tree Classifier
Both models are implemented using scikit-learn (sklearn).

**Features & Workflow**
**Web App Flow:**
**User Input:**
 Web form collects patient health details (age, cholesterol, blood pressure, etc).

**Model Prediction:**
 User submits form → Data fed into ML model → Returns heart disease prediction.

**Model Evaluation:**
 Accuracy, Confusion Matrix, and Feature Importance calculated and shown.

**Visualization:**
 Bar chart showing top important features influencing the prediction.

**Styling:**
 Responsive, colorful frontend with improved CSS.

**Key Results and Findings**
 Metric	Logistic Regression	Decision Tree
 Accuracy (on Test Set)	~82%	~79%
 Best Features	Cholesterol, Age, Max Heart Rate, ST Depression	Similar but decision tree more flexible
 Observations	Logistic Regression gives stable results, Decision Tree captures non-linearities	

**Technologies Used**
- Python
- Flask
- scikit-learn
- pandas
- numpy
- matplotlib / seaborn
- HTML5 / CSS3 (with styling for better user experience)

**Installation Instructions**
**Clone the repository:**

bash
Copy
Edit
git clone 
cd heart-disease-prediction-app
**Install dependencies:**

bash
Copy
Edit

**Run the Flask app:**
bash
Copy
Edit
python app.py
**Open in browser:**
cpp
Copy
Edit
http://127.0.0.1:5000/
**Screenshots**
![image](https://github.com/user-attachments/assets/1b10d01b-5f3f-400e-a564-07df14a71a3e)
![image](https://github.com/user-attachments/assets/46133e59-4278-437a-831f-21971c8991c4)



**Folder Structure:**
cpp
Copy
Edit
heart-disease-prediction/
├── app.py
├── templates/
│   └── index.html
├── static/
│   └── style.css
├── heart_cleveland_upload.csv
└── README.md

