# Define the ticker list
import pandas as pd
#tickers_list = ['TWTR', 'META','GOOG','AMZN','RYAAY']
tickers_list = ['TWTR']
# Fetch the data
import yfinance as yf
data = yf.download(tickers_list,'2016-5-1')['Adj Close']

# Print first 5 rows of the data
print(data.head())
# Plot all the close prices
((data.pct_change()+1).cumprod()).plot(figsize=(10, 7))

# Show the legend
plt.legend()

# Define the label for the title of the figure
plt.title("Returns", fontsize=16)

# Define the labels for x-axis and y-axis
plt.ylabel('Cumulative Returns', fontsize=14)
plt.xlabel('Year', fontsize=14)

# Plot the grid lines
plt.grid(which="major", color='k', linestyle='-.', linewidth=0.5)
plt.show()