import matplotlib.pyplot as plt
import pandas as pd

def plot_stock_data(data, column='Close'):
    """Plots the stock data."""
    plt.figure(figsize=(10, 6))
    plt.plot(data['Date'], data[column], label=column)
    plt.xlabel('Date')
    plt.ylabel(column)
    plt.title(f'Stock {column} Over Time')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    # Example usage
    data = pd.read_csv('data/processed/processed_stock_data.csv')
    plot_stock_data(data)
