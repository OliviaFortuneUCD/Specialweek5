import yfinance as yf
import datetime
import time
import requests
import io
data = yf.download(['GOOG','META'], period='1mo')
print(data.head)

my_list = data.columns.values.tolist()
print(my_list)
#print(data['Adj Close', 'GOOG'].max())
#print(data.max())
#print(data.max())
print(data.mean())