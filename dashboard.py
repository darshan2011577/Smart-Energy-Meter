import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from model import train_and_predict

st.title("⚡ Smart Energy Meter Dashboard")

# Load Data
data = pd.read_csv("energy_data.csv")
st.subheader("📊 Past Usage Data")
st.line_chart(data["Usage_kWh"])

# Predictions
predictions = train_and_predict()
st.subheader("🔮 Predicted Usage (Next 7 Days)")
st.write(predictions)

# Alerts
st.subheader("⚠️ Alerts")
for i, usage in enumerate(predictions, start=1):
    if usage > 9:
        st.error(f"High usage predicted on Day {i}: {usage:.2f} kWh")
