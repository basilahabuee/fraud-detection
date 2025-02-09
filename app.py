import streamlit as st
import numpy as np
import joblib

# Load trained model
model = joblib.load("fraud_detection_model.pkl")

st.title("Credit Card Fraud Detector")
input_data = st.text_input("Enter transaction details (comma-separated)")

if st.button("Predict"):
    data = np.array(input_data.split(",")).reshape(1, -1)
    prediction = model.predict(data)
    st.write("Fraudulent Transaction" if prediction == 1 else "Legitimate Transaction")