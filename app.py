import streamlit as st
import xgboost as xgb
import joblib
import numpy as np
import warnings

# Ignore warnings
warnings.filterwarnings("ignore", category=UserWarning)

# Load the trained model
model = joblib.load("fraud_detection_model.pkl")

# Streamlit App
st.title("Credit Card Fraud Detector")

# Input field
input_data = st.text_input("Enter transaction details (comma-separated)")

if st.button("Predict"):
    try:
        # Convert input data into a NumPy array with the correct number of features
        data = np.array([float(x) for x in input_data.split(",")]).reshape(1, -1)

        # Check if input size matches model expectation
        if data.shape[1] != model.n_features_in_:
            st.error(f"Expected {model.n_features_in_} features, but got {data.shape[1]}")
        else:
            # Make prediction
            prediction = model.predict(data)
            st.write("Fraudulent Transaction" if prediction == 1 else "Legitimate Transaction")

    except Exception as e:
        st.error(f"Error: {e}")