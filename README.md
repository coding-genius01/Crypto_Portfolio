# Coin Porfolio Application

## Overview
### The 'My Crypto Portfolio' is a python program designed to help users manage their cryptocurrency investments. With a user-friendly GUI created using tkinter and real-time coin data fetching via the requests library.

### Features
◉ Add Coins: Enter the coin's symbol, purchase price, and quantity to add it to your portfolio.
◉ Track Values: Automatically fetch current coin prices from an external API and display real-time value.
◉ Profit/Loss Calculation: View profit/loss per coin and the total portfolio P/L.
◉ Update Details: Modify the price or quantity of existing coins.
◉ Delete Coins: Remove coins from your portfolio.

## Prerequisites
### Python: You will need the Python source code and required libraries (tkinter, requests, sqlite3 and json).
### Internet Connection: Required for fetching real-time coin data.

## Usage

### Run the file using command prompt or a text editor of your choice.

### Add Coins:

Enter the coin symbol (e.g., BTC, ETH).
Enter the initial purchase price.
Enter the quantity purchased.
Click the "Add Coin" button to save the coin to your portfolio.

### Update Coins:

Choose an existing coin and enter its symbol, purchase price per coin and quantity.
Click the "Update Coin" button to save changes.

### Delete Coins:

Select a coin from the list and enter its Portfolio ID.
Click the "Delete Coin" button to remove it from your portfolio.

### View Portfolio:

The application will update and display the current value, profit/loss per coin, and total portfolio P/L with the press of the Refresh button.

## API Integration
The application fetches real-time coin prices using an external API. Ensure you have an active internet connection to retrieve the latest data. If you need to change the API endpoint or add support for other coins, you would need to modify the source code.

## Troubleshooting
No Data Displayed: Ensure you have a stable internet connection. There is an api-request limit of 10,000 per month.
Issues Adding/Updating Coins: Verify that all input fields are filled out correctly and the coin symbol is valid.
