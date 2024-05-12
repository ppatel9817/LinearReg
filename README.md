# Stock Price Prediction Using Linear Regression
This Python project demonstrates how to predict stock prices using linear regression by leveraging historical stock data from Yahoo Finance. The script fetches historical price data for specific stocks and uses linear regression to model the relationship between a stock's price and influential market indices.

Features
1. Fetch historical stock prices using yfinance.
2. Build a linear regression model to predict stock prices.
3. Evaluate model performance using metrics such as R-squared, MSE, RMSE, and MAE.
4. Predict future stock prices based on hypothetical market conditions.

Prerequisites
Before running this project, you will need the following:
Python 3.x
pip (Python package installer)

Configuration
To analyze different stocks or indices, modify the fetch_data function parameters in the stock_price_prediction.py script:

ticker: Set the stock ticker symbol according to Yahoo Finance (e.g., 'AAPL' for Apple Inc.).
start_date: Set the starting date for the historical data (format: 'YYYY-MM-DD').
end_date: Set the ending date for the historical data (format: 'YYYY-MM-DD').
