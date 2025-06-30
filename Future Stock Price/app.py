from flask import Flask, render_template, request
import yfinance as yf
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    plot_url = None
    error = None
    ticker_suggestions = ['AAPL', 'GOOGL', 'MSFT', 'TSLA', 'AMZN']
    if request.method == 'POST':
        ticker = request.form['ticker'].upper()
        model_choice = request.form['model']

        try:
            df = yf.download(ticker, start='2020-01-01', end='2025-06-28', progress=False)
            if df.empty:
                error = f"Ticker '{ticker}' not found or no data available. Please enter a valid ticker symbol."
                return render_template('index.html', result=result, plot_url=plot_url, error=error, ticker_suggestions=ticker_suggestions)
            df = df[['Open', 'High', 'Low', 'Close', 'Volume']].dropna()
            df['Target'] = df['Close'].shift(-1)
            df = df.dropna()
            X = df[['Open', 'High', 'Low', 'Volume']]
            y = df['Target']
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)
            if model_choice == 'Linear Regression':
                model = LinearRegression()
            else:
                model = RandomForestRegressor()

            model.fit(X_train, y_train)
            y_pred = model.predict(X_test)
            score = r2_score(y_test, y_pred)

            # Plot actual vs predicted
            plt.figure(figsize=(8,5))
            plt.plot(y_test.values, label='Actual Price', color='#1f77b4')
            plt.plot(y_pred, label='Predicted Price', color='#ff7f0e')
            plt.title(f'{ticker} Stock Price Prediction')
            plt.xlabel('Samples')
            plt.ylabel('Price')
            plt.legend()
            plt.tight_layout()

            if not os.path.exists('static'):
                os.makedirs('static')
            plot_path = os.path.join('static', 'plot.png')
            plt.savefig(plot_path)
            plt.close()

            result = f"R² Score: {score:.4f}"
            plot_url = plot_path
        except Exception as e:
            error = f"An error occurred: {str(e)}"

    return render_template('index.html', result=result, plot_url=plot_url, error=error, ticker_suggestions=ticker_suggestions)

if __name__ == '__main__':
    app.run(debug=True)
