import pandas as pd
import yfinance as yf
import datetime
import time
import requests
import io


aapl_df = yf.download('AAPL',
                      start='2022-01-01',
                      end='2022-05-16',
                      progress=False,
)
aapl_df.head()
print(aapl_df)