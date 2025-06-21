# app.py
import streamlit as st
import pickle
import numpy as np

# Load trained model and top 5 feature names
model = pickle.load(open('sales_model.pkl', 'rb'))
features = pickle.load(open('features.pkl', 'rb'))

# Set page config
st.set_page_config(page_title="Sales Prediction Dashboard", layout="centered")

# Title
st.title("🛒 Supermarket Sales Prediction Dashboard")
st.markdown("""
Welcome! Enter the values for the following features and click **Predict Sales** to get the predicted total revenue for a transaction.
""")

# Collect user input for each feature
user_input = []
for feature in features:
    value = st.number_input(f"🔢 {feature.replace('_', ' ').title()}", value=0.0, format="%.2f")
    user_input.append(value)

# Prediction Button
if st.button("Predict Sales"):
    input_array = np.array(user_input).reshape(1, -1)
    prediction = model.predict(input_array)[0]
    st.success(f"✅ Predicted Total Sales: ₹{prediction:.2f}")
