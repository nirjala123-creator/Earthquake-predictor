import streamlit as st
import pickle
import numpy as np

model = pickle.load(open('regression_model.pkl', 'rb'))
st.title("Earthquake Magnitude Predictor")

latitude = st.number_input("Latitude")
longitude = st.number_input("Longitude")
depth = st.number_input("Depth")
rms = st.number_input("Root Mean Square")
mag_type = st.number_input("Magnitude Type")
year = st.number_input("Year")
month = st.number_input("Month")
day = st.number_input("Day")
hour = st.number_input("Hour")

if st.button("Predict"):

    input_data = np.array([[
        latitude,
        longitude,
        depth,
        mag_type,
        rms,
        year,
        month,
        day,
        hour
    ]])

    prediction = model.predict(input_data)

    st.success(f"Predicted Magnitude: {prediction[0]:.2f}")

