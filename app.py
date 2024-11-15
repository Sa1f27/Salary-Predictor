import streamlit as st
import pickle
import numpy as np

# Load the pre-trained model
with open(r"C:\Users\huzai\pycharm_projects\linear_regression_model.pkl", "rb") as file:
    model = pickle.load(file)

# Streamlit App Title
st.title("Salary Predictor")

# Input field for years of experience
years = st.number_input("Enter Years of Experience", min_value=1.0, max_value=50.0, value=20.0, step=0.5)

# Prediction button
if st.button("Predict"):
    experience = np.array([[years]])
    pred = model.predict(experience)

    # Display the prediction result
    st.success(f"Your predicted salary would be: ${pred[0]:,.2f}")
