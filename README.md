# AI-ML-Intership-Tasks
# Task 01
📈 Stock Price Prediction Web App (Short-Term Forecasting)
A Flask-based web application that uses historical stock market data from Yahoo Finance to predict the next day's closing price for any given stock ticker (e.g., Apple, Tesla).
This project demonstrates time series handling, regression modeling, and data visualization.

✅ Task Objective
- Build a machine learning model to predict the next day's closing stock price based on historical data.
- Allow users to select stock ticker symbols (like AAPL, TSLA, GOOGL) and choose between Linear Regression and Random Forest models.
- Provide an interactive web interface for input and result visualization.
- Display Actual vs Predicted stock prices for test data.

**✅ Dataset Used**
Source: Yahoo Finance
Library Used for Data Retrieval: yfinance
Data Fields Used:
- Open
- High
- Low
- Volume
- Close (as target: next day’s close)

**✅ Features and Workflow**
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

**✅ Models Applied**
- Linear Regression
- Random Forest Regressor
Both models are implemented using scikit-learn.

**✅ Key Results and Findings**
**Metric**	**Result**
**Prediction Goal**	Next day's closing price
**Evaluation Metric**	R² Score
Visualization	Actual vs Predicted Close Price Graph
**Test Results**	Models typically achieved R² Scores ranging between 0.6 - 0.9 depending on stock and time period. Random Forest often performed better on noisy stocks.
Finding	Including features like Open, High, Low, and Volume helps in capturing stock movement patterns for short-term prediction. However, stock market data is inherently noisy, so model performance varies per stock.

**✅ Screenshots**
(Add screenshots of your app UI and Actual vs Predicted plot here if needed)

**✅ Technologies Used**
- Python
- Flask
- yfinance
- pandas
- numpy
- scikit-learn
- matplotlib
- HTML5 / CSS3 (Responsive, Gradient, Animated)
