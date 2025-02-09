import xgboost as xgb
import joblib
import numpy as np

# Load the trained model
model = joblib.load("fraud_detection_model.pkl")

# Create a test input with the correct number of features
test_input = np.random.rand(1, model.n_features_in_)  # Generate random values

# Try predicting
prediction = model.predict(test_input)
print("Test Prediction:", prediction)