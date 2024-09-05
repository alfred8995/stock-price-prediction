import pandas as pd
from sklearn.metrics import mean_squared_error
import joblib

def evaluate_model(data, target_column='Close'):
    """Evaluates the trained model on test data."""
    model = joblib.load('models/stock_price_predictor.pkl')
    X = data.drop(columns=[target_column])
    y = data[target_column]
    
    predictions = model.predict(X)
    mse = mean_squared_error(y, predictions)
    
    print(f"Mean Squared Error: {mse}")

if __name__ == "__main__":
    # Example usage
    data = pd.read_csv('data/processed/processed_stock_data.csv')
    evaluate_model(data)
