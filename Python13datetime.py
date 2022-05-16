import pandas as pd
import yfinance as yf
import datetime
import time
import requests
import io


ticker = yf.Ticker('AAPL')
aapl_df = ticker.history(period="5y")
aapl_df['Close'].plot(title="APPLE's stock price")