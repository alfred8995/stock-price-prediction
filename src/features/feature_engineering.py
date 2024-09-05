import pandas as pd

def generate_moving_average(data, window=5):
    """Generates moving average as a new feature."""
    data[f'moving_average_{window}'] = data['Close'].rolling(window=window).mean()
    return data

def generate_rsi(data, period=14):
    """Generates RSI (Relative Strength Index) as a new feature."""
    delta = data['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
    rs = gain / loss
    data['RSI'] = 100 - (100 / (1 + rs))
    return data
