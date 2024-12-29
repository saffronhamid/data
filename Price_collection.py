import yfinance as yf
import pandas as pd

def get_stock_price_data(ticker, start_date, end_date):
    """
    Fetch historical price data for a given stock ticker.
    
    :param ticker: Stock ticker symbol (e.g., AAPL, TSLA).
    :param start_date: Start date for fetching historical data (YYYY-MM-DD).
    :param end_date: End date for fetching historical data (YYYY-MM-DD).
    :return: DataFrame with Date and Close Price.
    """
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    if not stock_data.empty:
        return stock_data[['Close']].reset_index()
    else:
        print(f"No data found for {ticker}.")
        return None

def save_to_csv(ticker, data):
    """
    Saves the price data to a CSV file.
    
    :param ticker: Stock ticker symbol.
    :param data: DataFrame with stock price data.
    """
    filename = f"{ticker}_price_data.csv"
    data.to_csv(filename, index=False)
    print(f"Saved price data for {ticker} to {filename}.")

def main():
    stock_symbols = ["AAPL", "GOOGL", "MSFT","GLD"]  # Add your stock symbols here
    start_date = "2023-01-01"  # Specify the start date
    end_date = "2023-12-31"    # Specify the end date
    
    for ticker in stock_symbols:
        print(f"Fetching price data for {ticker}...")
        data = get_stock_price_data(ticker, start_date, end_date)
        if data is not None:
            save_to_csv(ticker, data)

if __name__ == "__main__":
    main()
