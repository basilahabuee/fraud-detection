Credit Card Fraud Detection

Table of Contents:
1. Overview
2. Dataset
3. How It Works
4. Installation
5. Usage
6. Model Information
7. Technologies Used
8. Author
9. License

Overview
This project is a machine learning-based fraud detection system that identifies fraudulent credit card transactions. The model is trained on real-world transaction data and deployed using Streamlit, allowing users to input transaction details and receive a fraud prediction.

Dataset
The dataset used for training is the Credit Card Fraud Detection Dataset from Kaggle. It contains anonymized transaction data with labels indicating whether a transaction is fraudulent (1) or legitimate (0).

How It Works
1. Users enter transaction details in the Streamlit web app.
2. The trained XGBoost model processes the input.
3. The model predicts whether the transaction is fraudulent or legitimate.
4. The result is displayed on the screen.

Installation
Prerequisites
Python installed on your system

Clone the Repository
git clone https://github.com/basilahabuee/fraud-detection.git
cd fraud-detection

Install Dependencies
pip install -r requirements.txt

Run the Application Locally
streamlit run app.py

Usage
You can test the application live at:
https://my-fraud-detection.streamlit.app/

Steps to Use:
1. Open the Streamlit app using the link above.
2.Enter transaction details in the input box.
3. Click the Predict button to check if the transaction is fraudulent.

Model Information
Algorithm Used: XGBoost (Extreme Gradient Boosting)
Evaluation Metric: AUC Score (0.93)
Data Processing: Features are normalized before training

Technologies Used
Python (Programming Language)
XGBoost (Machine Learning Model)
Streamlit (Web App Framework)
NumPy, Pandas (Data Processing)
Joblib (Model Serialization)

Author
Name: Basil Ahabue
GitHub: basilahabuee
License
This project is licensed under the MIT License.

