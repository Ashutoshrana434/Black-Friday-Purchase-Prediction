import streamlit as st
import pandas as pd
import joblib

# Load the trained brain
model = joblib.load('black_friday_model.pkl')

st.title("Black Friday Sales Predictor")
st.write("Predict how much a customer is likely to spend.")

# User Inputs
col1, col2 = st.columns(2)

with col1:
    gender = st.selectbox("Gender", ["Male", "Female"])
    age = st.selectbox("Age Group", ["0-17", "18-25", "26-35", "36-45", "46-50", "51-55", "55+"])
    occupation = st.slider("Occupation Code", 0, 20, 10)

with col2:
    city = st.selectbox("City Category", ["A", "B", "C"])
    stay = st.selectbox("Years in Current City", ["0", "1", "2", "3", "4+"])
    marital = st.selectbox("Marital Status", ["Unmarried", "Married"])

# Category inputs
p1 = st.number_input("Product Category 1", 1, 20, 1)
p2 = st.number_input("Product Category 2", 0, 20, 0)
p3 = st.number_input("Product Category 3", 0, 20, 0)

# Preprocessing for Prediction
if st.button("Predict Purchase Amount"):
    # Convert inputs to the numeric format the model expects
    input_data = pd.DataFrame([[
        1 if gender == "Male" else 0,
        {"0-17":0, "18-25":1, "26-35":2, "36-45":3, "46-50":4, "51-55":5, "55+":6}[age],
        occupation,
        {"A":0, "B":1, "C":2}[city],
        {"0":0, "1":1, "2":2, "3":3, "4+":4}[stay],
        1 if marital == "Married" else 0,
        p1, p2, p3
    ]], columns=['Gender', 'Age', 'Occupation', 'City_Category', 
                 'Stay_In_Current_City_Years', 'Marital_Status', 
                 'Product_Category_1', 'Product_Category_2', 'Product_Category_3'])
    
    prediction = model.predict(input_data)
    st.success(f"### Estimated Spend: ₹{prediction[0]:,.2f}")