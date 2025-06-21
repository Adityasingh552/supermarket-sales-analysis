# app.py
import streamlit as st
import pickle
import numpy as np

# Load model and features
model = pickle.load(open('sales_model.pkl', 'rb'))
features = pickle.load(open('features.pkl', 'rb'))

st.title("💰 Supermarket Sales Prediction")

# Input fields for top 5 features
inputs = []
for feature in features:
    val = st.number_input(f"Enter value for {feature}:", step=1.0)
    inputs.append(val)

# Predict button
if st.button("Predict Sales"):
    data = np.array(inputs).reshape(1, -1)
    prediction = model.predict(data)[0]
    st.success(f"✅ Predicted Total Sales: ₹{prediction:.2f}")
