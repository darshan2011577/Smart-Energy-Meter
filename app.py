import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader

# ---------------------------
# Function to generate PDF
# ---------------------------
def create_pdf():
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)
    width, height = A4

    # Title
    c.setFont("Helvetica-Bold", 16)
    c.drawString(100, height - 50, "🔋 Smart Energy Meter")

    # Developer Info
    c.setFont("Helvetica", 12)
    c.drawString(100, height - 100, "Developed by: Darshan JR")

    # Add photo
    try:
        img = Image.open("darshan_photo.jpeg")
        img = img.resize((120, 120))  # Resize photo
        c.drawImage(ImageReader(img), width - 200, height - 180, 120, 120)
    except:
        c.setFont("Helvetica", 10)
        c.drawString(100, height - 120, "⚠️ Photo not found. Please place 'darshan_photo.jpeg' in the same folder.")

    # Project Details
    text = c.beginText(100, height - 220)
    text.setFont("Helvetica", 11)
    lines = [
        "📘 Project Description",
        "The Smart Energy Meter is a modern solution for monitoring and managing electricity consumption.",
        "It enables real-time tracking of power usage, provides analytical insights, and promotes conservation.",
        "",
        "🛠️ Tools & Technologies Used:",
        "- Programming Language: Python",
        "- Framework: Streamlit",
        "- Libraries: Pandas, NumPy, Matplotlib, PIL",
        "- Version Control: Git & GitHub",
        "",
        "✨ Key Features:",
        "- Real-time electricity usage monitoring",
        "- Graphical visualization of power consumption",
        "- Cost estimation and billing prediction",
        "- User-friendly web interface",
        "",
        "✅ Conclusion:",
        "This project integrates software and energy management, helping users track and optimize their energy usage."
    ]
    for line in lines:
        text.textLine(line)
    c.drawText(text)

    c.showPage()
    c.save()
    buffer.seek(0)
    return buffer

# ---------------------------
# Sidebar Profile Section
# ---------------------------
st.sidebar.image("darshan_photo.jpeg", caption="Darshan JR", use_container_width=True)
st.sidebar.title("🔋 Smart Energy Meter")
st.sidebar.markdown("Developed by **Darshan JR**")
st.sidebar.markdown("---")

# ---------------------------
# Main Title
# ---------------------------
st.title("🔋 Smart Energy Meter")
st.markdown("### Developed by Darshan JR")

# ---------------------------
# Project Description
# ---------------------------
st.subheader("📘 Project Description")
st.write("""
The Smart Energy Meter is a modern solution for monitoring and managing household and 
industrial electricity consumption. It enables real-time tracking of power usage, 
provides analytical insights, and promotes energy conservation.
""")

# ---------------------------
# Tools Used
# ---------------------------
st.subheader("🛠️ Tools & Technologies Used")
st.write("""
- **Programming Language**: Python  
- **Framework**: Streamlit  
- **Libraries**: Pandas, NumPy, Matplotlib, PIL  
- **Version Control**: Git & GitHub  
""")

# ---------------------------
# Key Features
# ---------------------------
st.subheader("✨ Key Features")
st.write("""
- Real-time electricity usage monitoring  
- Graphical visualization of power consumption  
- Cost estimation and billing prediction  
- User-friendly web interface  
""")

# ---------------------------
# Demo: Simulated Power Consumption Data
# ---------------------------
st.subheader("📊 Power Consumption Demo")

# Generate sample data
days = np.arange(1, 8)
usage = np.random.randint(2, 10, size=7)  # Random kWh usage

df = pd.DataFrame({"Day": days, "Usage (kWh)": usage})

st.dataframe(df)

# Plot
fig, ax = plt.subplots()
ax.plot(df["Day"], df["Usage (kWh)"], marker="o", linestyle="-")
ax.set_title("Weekly Power Consumption")
ax.set_xlabel("Day")
ax.set_ylabel("Usage (kWh)")
st.pyplot(fig)

# ---------------------------
# Conclusion
# ---------------------------
st.subheader("✅ Conclusion")
st.write("""
This project demonstrates the integration of software and energy management, providing users with 
a smart and interactive system to track and optimize their energy usage.
""")

# ---------------------------
# Download PDF Button
# ---------------------------
st.download_button(
    label="📥 Download Project Report (PDF)",
    data=create_pdf(),
    file_name="Smart_Energy_Meter_Report.pdf",
    mime="application/pdf"
)
