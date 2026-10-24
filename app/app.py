import streamlit as st, joblib, pandas as pd

model = joblib.load("./notebooks/model.joblib")

st.title("🏠 House Price Predictor")
st.write("Enter the house area to get an estimated price.")

area = st.number_input("Area (sq ft)", min_value=100, max_value=10000, value=1500, step=50)

if st.button("Predict"):
    price = model.predict(pd.DataFrame({"area": [area]}))[0]
    st.success(f"Estimated price: ₹{price:,.0f}")