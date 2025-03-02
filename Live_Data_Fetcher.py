#How the Script Works:
#Fetches Live Data: The script uses the CoinGecko API to fetch real-time cryptocurrency data.
#Processes Data: The data is structured into a pandas DataFrame with proper formatting.
#Updates Google Sheets: The script clears the existing data and updates it with fresh information.
#Runs on a Loop: The script continuously updates data every 5 minutes.

import pandas as pd
import gspread
from google.oauth2.service_account import Credentials
from pycoingecko import CoinGeckoAPI
import time

# Google Sheets API Setup
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
SERVICE_ACCOUNT_FILE = "/glass-mantra-452505-i4-bcf6c675c0ae.json"  # Replace with your JSON key file

# Authenticate and open Google Sheet
gs_credentials = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
client = gspread.authorize(gs_credentials)


# Open the Google Sheet by URL
sheet = client.open_by_url("https://docs.google.com/spreadsheets/d/1UrxKLJeau_-golZ0GdddcGMdNAC-7FBmp7nvNqWdxBg/edit?usp=sharing").sheet1  # Replace with your Sheet URL


# Create an instance of the CoinGeckoAPI class
cg = CoinGeckoAPI()

# Function to fetch live cryptocurrency data and update Google Sheet
def fetch_and_update_google_sheets():
    while True:
      # Retrieve data for the top 50 cryptocurrencies
        crypto_data = cg.get_coins_markets(vs_currency="usd", order="market_cap_desc", per_page=50, page=1, sparkline=False)
        
        # Convert the retrieved data into a pandas DataFrame
        data = pd.DataFrame(crypto_data, columns=["name", "symbol", "current_price", "market_cap", "total_volume", "price_change_percentage_24h", "last_updated"])
        
        # Rename columns for better readability
        data.columns = ["Cryptocurrency Name", "Symbol", "Current Price (USD)", "Market Capitalization", "24h Trading Volume", "Price Change (24h %)", "Last Updated"]

        # Convert "Last Updated" to datetime format
        data["Last Updated"] = pd.to_datetime(data["Last Updated"])

        # Convert 'Last Updated' column to strings before appending to Google Sheets
        data["Last Updated"] = data["Last Updated"].dt.strftime('%Y-%m-%d %H:%M:%S') # Convert Timestamp objects to strings

        # Update Google Sheets
        sheet.clear()
        sheet.append_row(data.columns.tolist())
        sheet.append_rows(data.values.tolist())

        
        print("Google Sheet updated with latest cryptocurrency data.")
        
        # Wait for 5 minutes before fetching the data again
        time.sleep(300)
        
# Start live updating the Google Sheet
fetch_and_update_google_sheets()
