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
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import io

# Function to generate project report PDF
def create_project_report():
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer, pagesize=A4)
    width, height = A4

    # Title
    p.setFont("Helvetica-Bold", 20)
    p.drawCentredString(width/2, height - 100, "Smart Energy Meter Project Report")

    # Content
    p.setFont("Helvetica", 12)
    text = p.beginText(50, height - 150)
    text.textLine("This report presents the Smart Energy Meter Project developed using Python & Streamlit.")
    text.textLine("")
    text.textLine("The project demonstrates real-time monitoring of energy consumption,")
    text.textLine("provides visualization dashboards, and applies AI techniques for analysis.")
    text.textLine("")
    text.textLine("The system aims to promote efficient energy management for households and industries.")
    text.textLine("")
    text.textLine("-------------------------------------------------------------")
    text.textLine("Special Acknowledgement")
    text.textLine("-------------------------------------------------------------")
    text.textLine("")
    text.textLine("We extend our heartfelt gratitude to our constant motivator,")
    text.textLine("Dr. Vijayraj (Asst. Professor, AI&DS Dept),")
    text.textLine("for his unwavering guidance, encouragement, and valuable insights,")
    text.textLine("which inspired us throughout the development of this project.")
    text.textLine("")
    text.textLine("His mentorship has been a beacon of knowledge and motivation,")
    text.textLine("helping us transform our ideas into reality.")
    text.textLine("")
    text.textLine("We proudly dedicate this project report as a token of respect and")
    text.textLine("gratitude for his invaluable support.")
    p.drawText(text)

    p.showPage()
    p.save()
    buffer.seek(0)
    return buffer

# Add Download button in Streamlit
st.subheader("📄 Project Report")
pdf_buffer = create_project_report()
st.download_button(
    label="⬇️ Download Project Report",
    data=pdf_buffer,
    file_name="Smart_Energy_Meter_Report.pdf",
    mime="application/pdf"
)

