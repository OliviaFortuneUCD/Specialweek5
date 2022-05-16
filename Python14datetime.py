import yfinance as yf
import datetime
import time
import requests
import io
data = yf.download(['GOOG','META'], period='1mo')
data.head()
print(data.head)