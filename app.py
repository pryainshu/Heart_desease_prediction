import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open("model.pkl", "rb"))

st.title("Heart Disease Prediction App")

st.write("Enter patient details:")

# Example inputs (change according to your dataset)
age = st.number_input("Age", 1, 120, 50)
sex = st.selectbox("Sex", [0, 1])  
cp = st.selectbox("Chest Pain Type (cp)", [0, 1, 2, 3])
trestbps = st.number_input("Resting Blood Pressure", 80, 200, 120)
chol = st.number_input("Cholesterol", 100, 400, 200)

# Convert to array
input_data = np.array([[age, sex, cp, trestbps, chol]])

if st.button("Predict"):
    prediction = model.predict(input_data)
    if prediction[0] == 1:
        st.error("⚠️ The model predicts a **high chance of heart disease**.")
    else:
        st.success("✅ The model predicts **low chance of heart disease**.")
        