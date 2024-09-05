import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib

def train_model(data, target_column='Close'):
    """Trains a Linear Regression model to predict stock prices."""
    X = data.drop(columns=[target_column])
    y = data[target_column]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    joblib.dump(model, 'models/stock_price_predictor.pkl')
    return model

if __name__ == "__main__":
    # Example usage
    data = pd.read_csv('data/processed/processed_stock_data.csv')
    model = train_model(data)
