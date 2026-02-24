import streamlit as st
import joblib
import pandas as pd

# Load files
from xgboost import XGBRegressor
import joblib

model = XGBRegressor()
model.load_model("black_friday_model.json")

encoders = joblib.load("encoders.pkl")
model_columns = joblib.load("model_columns.pkl")

print("ENCODER TYPE:", type(encoders))
print("ENCODER CONTENT:", encoders)

st.title("Black Friday Purchase Prediction")

gender = st.selectbox("Gender", ["M", "F"])
age = st.selectbox("Age", ["0-17", "18-25", "26-35", "36-45", "46-50", "51-55", "55+"])
occupation = st.number_input("Occupation", min_value=0,max_value=20)
product1 = st.number_input("Product Category 1", min_value=1, max_value=20)
product2 = st.number_input("Product Category 2 (0 if NA)", min_value=0, max_value=20)
product3 = st.number_input("Product Category 3 (0 if NA)", min_value=0, max_value=20)
city = st.selectbox("City Category", ["A", "B", "C"])
stay = st.selectbox("Years in Current City", ["0", "1", "2", "3", "4+"])

if st.button("Predict"):
    input_dict = {
    "Gender": gender,
    "Age": age,
    "Occupation": occupation,
    "City_Category": city,
    "Stay_In_Current_City_Years": stay,
    "Product_Category_1": product1,
    "Product_Category_2": product2,
    "Product_Category_3": product3
}
    input_df = pd.DataFrame([input_dict])

    # ---- APPLY LABEL ENCODERS (MOST IMPORTANT FIX) ----
    for col in ['Gender', 'Age', 'City_Category']:
        input_df[col] = encoders[col].transform(input_df[col])

    # ---- ONE HOT ENCODE ONLY CITY YEARS ----
    input_df = pd.get_dummies(input_df, columns=['Stay_In_Current_City_Years'])

    # ---- MATCH TRAINING COLUMNS ----
    input_df = input_df.reindex(columns=model_columns, fill_value=0)

    # ---- PREDICT ----
    prediction = model.predict(input_df)

    st.success(f"Predicted Purchase: ₹{float(prediction[0]):,.2f}")