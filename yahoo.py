import yfinance as yf
import ssl
import matplotlib.pyplot as plt
import csv
import pandas as pd
import datetime as dt

comp = yf.Ticker("AAPL")

# get historical market data
hist = comp.history(period="1y")
print(hist)
start = dt.datetime(2020, 1, 1)
end = dt.datetime.now()

# Download stock data then export as CSV
data_df = yf.download("AAPL", start, end)
data_df.to_csv('/Users/snehabarve/Documents/MISC/Stocks_dataset/AAPL_stock.csv')

