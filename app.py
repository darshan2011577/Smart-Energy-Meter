import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

# Title
st.title("⚡ Smart Energy Meter Dashboard")

# Sidebar
st.sidebar.header("Navigation")
option = st.sidebar.radio("Go to", ["Home", "Upload Data", "Analysis", "Prediction"])

# Home
if option == "Home":
    st.subheader("Welcome to Smart Energy Meter Dashboard")
    st.image("darshan_photo.jpeg", caption="Darshan JR", width=200)
    st.write("""
    This is a working model of a **Smart Energy Meter System**  
    developed using **Python, Streamlit, and Machine Learning**.
    """)

# Upload Data
elif option == "Upload Data":
    st.subheader("Upload your CSV data")
    uploaded_file = st.file_uploader("Choose a file", type=["csv"])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.dataframe(df)

# Analysis
elif option == "Analysis":
    st.subheader("Data Analysis")
    uploaded_file = st.file_uploader("Upload CSV for Analysis", type=["csv"])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write("### Dataset Preview")
        st.dataframe(df.head())
        st.write("### Summary Statistics")
        st.write(df.describe())
        st.write("### Consumption Trend")
        df.plot()
        st.pyplot(plt)

# Prediction
elif option == "Prediction":
    st.subheader("Energy Consumption Prediction")
    X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
    y = np.array([2, 4, 6, 8, 10])
    model = LinearRegression()
    model.fit(X, y)
    prediction = model.predict([[6]])
    st.write(f"Predicted consumption for day 6: {prediction[0]} units")

# --- Motivator Footer ---
st.markdown("---")
st.markdown(
    "<h4 style='text-align: center; color: green;'>"
    "🌟 My Constant Motivator: <b>Dr. Vijayraj</b><br>(Asst. Prof, AI&DS Dept)"
    "</h4>",
    unsafe_allow_html=True
)
