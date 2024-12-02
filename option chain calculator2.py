import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

def get_option_chain(ticker: str, expiration_date: str):
    # Get the stock object
    stock = yf.Ticker(ticker)
    
    # Fetch the option chain for the given expiration date
    option_chain = stock.option_chain(expiration_date)
    
    # Get Calls and Puts data
    calls = option_chain.calls
    puts = option_chain.puts
    
    return calls, puts

def display_option_chain(calls, puts):
    print("\nCalls Data:")
    print(calls[['strike', 'lastPrice', 'bid', 'ask', 'openInterest', 'impliedVolatility']])
    
    print("\nPuts Data:")
    print(puts[['strike', 'lastPrice', 'bid', 'ask', 'openInterest', 'impliedVolatility']])


def get_expiration_dates(ticker: str):
    stock = yf.Ticker(ticker)
    return stock.options

def plot_option_chain(calls, puts):
    # Plotting Open Interest for Calls
    plt.figure(figsize=(12, 6))
    
    plt.subplot(1, 2, 1)
    plt.plot(calls['strike'], calls['openInterest'], label='Call Open Interest', color='green')
    plt.xlabel('Strike Price')
    plt.ylabel('Open Interest')
    plt.title('Call Option Open Interest')

    # Plotting Open Interest for Puts
    plt.subplot(1, 2, 2)
    plt.plot(puts['strike'], puts['openInterest'], label='Put Open Interest', color='red')
    plt.xlabel('Strike Price')
    plt.ylabel('Open Interest')
    plt.title('Put Option Open Interest')

    plt.tight_layout()
    plt.show()

def main():
    ticker = input("Enter the stock ticker (e.g., AAPL,TSLA,PAYPAL,GENERAL MOTORS,FADEX,IBM etc.): ")
    
    # Fetch expiration dates
    expirations = get_expiration_dates(ticker)
    print(f"Available Expiration Dates: {expirations}")
    
    expiration_date = input("Enter an expiration date (e.g., '2024-12-25'): ")
    
    # Get the option chain data
    calls, puts = get_option_chain(ticker, expiration_date)
    
    # Display the data
    display_option_chain(calls, puts)
    
    # Plot the option chain
    plot_option_chain(calls, puts)

if __name__ == "__main__":
    main()
