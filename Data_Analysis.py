#Data Analysis:
#This script also performs basic analysis on the fetched cryptocurrency data:
#1.Identifies the top 5 cryptocurrencies by market capitalization.
#2.Calculates the average price of the top 50 cryptocurrencies.
#3.Analyzes the highest and lowest 24-hour percentage price changes among the top 50 cryptocurrencies.

import pandas as pd
import matplotlib.pyplot as plt
from pycoingecko import CoinGeckoAPI
import time
import math

# Create an instance of the CoinGeckoAPI class
cg = CoinGeckoAPI()

# Check API connectivity
cg.ping()

# Retrieve data for the top 50 cryptocurrencies
crypto_data = cg.get_coins_markets(vs_currency="usd", order="market_cap_desc", per_page=50, page=1, sparkline=False)

# Convert the retrieved data into a pandas DataFrame
data = pd.DataFrame(crypto_data, columns=["name", "symbol", "current_price", "market_cap", "total_volume", "price_change_percentage_24h", "last_updated"])

# Convert "last_updated" to datetime format
data["last_updated"] = pd.to_datetime(data["last_updated"])

# Rename columns for better readability
data.columns = ["Cryptocurrency Name", "Symbol", "Current Price (USD)", "Market Capitalization", "24h Trading Volume", "Price Change (24h %)", "Last Updated"]

# Identify the top 5 cryptocurrencies by market capitalization
top_5_market_cap = data.nlargest(5, "Market Capitalization")

# Calculate the average price of the top 50 cryptocurrencies
average_price = data["Current Price (USD)"].mean()

# Find the highest and lowest 24-hour percentage price change
highest_24h_change = data.loc[data["Price Change (24h %)"].idxmax()]
lowest_24h_change = data.loc[data["Price Change (24h %)"].idxmin()]

# Display analysis results
print("\nTop 50 Cryptocurrencies Data:\n")
print(data.to_string(index=False))

print("\nTop 5 Cryptocurrencies by Market Cap:\n")
print(top_5_market_cap.to_string(index=False))

print(f"\nAverage Price of Top 50 Cryptocurrencies: ${average_price:.2f}")

print("\nHighest 24h Percentage Price Change:")
print(highest_24h_change.to_string())

print("\nLowest 24h Percentage Price Change:")
print(lowest_24h_change.to_string())
