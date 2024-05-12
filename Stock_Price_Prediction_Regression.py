#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 12 10:21:31 2024

@author: poojanpatel
"""

import yfinance as yf
import pandas as pd
import numpy as np
import statsmodels.api as sm
from datetime import datetime
from sklearn.metrics import mean_squared_error, mean_absolute_error

# Function to fetch historical data
def fetch_data(ticker, start_date, end_date):
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    return stock_data['Adj Close']

# Fetching data
start_date = '2020-01-01'
end_date = datetime.now().strftime('%Y-%m-%d')  # current date
aapl_data = fetch_data('JPM', start_date, end_date)
gspc_data = fetch_data('^GSPC', start_date, end_date)

# Combining data into a single DataFrame
data = pd.DataFrame({
    'JPM': aapl_data,
    'GSPC': gspc_data
})

# Handling missing data
data.fillna(method='ffill', inplace=True)  # Forward fill to handle missing values
data.dropna(inplace=True)  # Drop any remaining NaNs

# Regression analysis
X = sm.add_constant(data['GSPC'])  # adding a constant for intercept
y = data['JPM']

# Fit the linear regression model
model = sm.OLS(y, X).fit()

# Model summary
print(model.summary())

# Prediction and accuracy assessment
predictions = model.predict(X)
mse = mean_squared_error(y, predictions)
rmse = np.sqrt(mse)
mae = mean_absolute_error(y, predictions)

print("\nAccuracy Metrics:")
print("Mean Squared Error (MSE):", mse)
print("Root Mean Squared Error (RMSE):", rmse)
print("Mean Absolute Error (MAE):", mae)

# Prediction example - predict AAPL price based on a hypothetical S&P 500 index value
new_index_value = pd.DataFrame({'const': [1], 'GSPC': [4000]})  # Hypothetical S&P 500 index value
predicted_price = model.predict(new_index_value)
print("\nPredicted JPM Stock Price for S&P 500 at 4000: ", predicted_price[0])
