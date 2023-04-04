import yfinance as yf
import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Get user input
ticker = st.text_input('Enter Ticker Symbol:', 'AAPL')

# Download stock data using yfinance
data = yf.download(ticker, start="2015-01-01", end="2023-03-17")

# Create a dataframe with just the closing price
df = pd.DataFrame(data=data, columns=['Close'])

# Calculate the 50-day moving average
df['MA50'] = df['Close'].rolling(window=50).mean()

# Add a column for the daily price change
df['Daily Change'] = df['Close'].pct_change()

# Drop any rows with missing data
df.dropna(inplace=True)

# Set X and y variables for linear regression
X = df[['MA50', 'Daily Change']]
y = df['Close']

# Create a linear regression object and fit the model
model = LinearRegression()
model.fit(X, y)

# Use the model to predict the next day's closing price
next_day = np.array([df['MA50'].iloc[-1], df['Daily Change'].iloc[-1]]).reshape(1, -1)
prediction = model.predict(next_day)

# Plot the stock price data and linear regression line
fig, ax = plt.subplots()
ax.plot(df['Close'], label='Actual')
ax.plot(df.index, model.predict(X), label='Predicted')
ax.legend()
ax.set_xlabel('Date')
ax.set_ylabel('Price')
ax.set_title(f'{ticker} Stock Price and Predicted Price')
st.pyplot(fig)

# Output the prediction using streamlit
st.write(f"Predicted Closing Price for {ticker} tomorrow is: {prediction[0]:.2f}")
