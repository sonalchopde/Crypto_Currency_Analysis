# Crypto Live Data Fetcher

## Overview
This Python script fetches live cryptocurrency data for the **top 50 cryptocurrencies** by market capitalization using the **CoinGecko API**. It updates a **Google Spreadsheet** in real-time every **5 minutes** with key cryptocurrency metrics, ensuring that the data remains up to date.

## Features
- Fetches **live data** for the top 50 cryptocurrencies.
- Includes key metrics such as:
  - Cryptocurrency Name
  - Symbol
  - Current Price (USD)
  - Market Capitalization
  - 24h Trading Volume
  - 24h Percentage Price Change
  - Last Updated Time
- **Updates Google Sheets** automatically every 5 minutes.
- Uses the **Google Sheets API** for data storage.
- Supports **error handling** for API failures and connection issues.
- **Data is formatted** properly in Google Sheets for better readability.

## Prerequisites
### 1. Install Required Libraries
Ensure you have Python 3 installed, then install the dependencies:
pip install pandas gspread google-auth pycoingecko

### 2. Enable Google Sheets API
- Go to **Google Cloud Console**.
- Enable the **Google Sheets API**.
- Generate a **Service Account JSON key** and download it.

### 3. Share Google Spreadsheet with the Service Account
- Open your **Google Spreadsheet**.
- Click **Share**.
- Add the **service account email** from your JSON key as an **Editor**.

## Setup and Usage
1. **Clone the Repository:**
git clone https://github.com/your-username/crypto-live-data.git
cd crypto-live-data
2. **Place the JSON Key File** in the project directory and update the script:
python
SERVICE_ACCOUNT_FILE = "your-service-key.json"
3. **Run the Script:**
python script.py

## Google Sheets Integration
The script will automatically update your Google Spreadsheet with the latest cryptocurrency data. Ensure that:
- The Google Sheet URL is correctly set in the script.
- The **service account** has editor access to modify the spreadsheet.
- The script runs continuously to keep data updated.

## Security Best Practices
⚠️ **Do not upload your JSON key file to GitHub!** Add the following to `.gitignore`:
*.json
Alternatively, use environment variables to securely store the path to your JSON key.

## Troubleshooting
### Common Issues & Fixes:
- **403 Permission Denied:** Ensure the **service account** has access to the Google Sheet.
- **API Rate Limits:** CoinGecko may restrict excessive requests. Reduce the update frequency if needed.
- **Google Sheets Not Updating:** Double-check the authentication and spreadsheet ID.

## Future Improvements
- Implement a **dashboard** using Flask or Streamlit for real-time visualization.
- Add **alerts/notifications** when significant price changes occur.
- Expand to support multiple fiat currencies (USD, EUR, etc.).
- Optimize the script for better performance and scalability.

## Author
**Sonal Chopde**


