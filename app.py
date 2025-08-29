import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

# -------------------------------
# Title
# -------------------------------
st.title("🔌 Smart Energy Meter Project")

st.write(
    "This is a demo Smart Energy Meter web app built with Streamlit. "
    "It shows simulated energy consumption data and allows downloading "
    "a project report in PDF format."
)

# -------------------------------
# Generate sample energy data
# -------------------------------
days = pd.date_range(start="2025-01-01", periods=7, freq="D")
usage = np.random.randint(2, 10, size=7)

df = pd.DataFrame({"Day": days, "Energy Usage (kWh)": usage})

# Display table
st.subheader("📊 Weekly Energy Usage Data")
st.dataframe(df, use_container_width=True)

# Display chart
st.subheader("📈 Energy Usage Chart")
fig, ax = plt.subplots()
ax.plot(df["Day"], df["Energy Usage (kWh)"], marker="o")
ax.set_xlabel("Day")
ax.set_ylabel("Energy Usage (kWh)")
ax.set_title("Weekly Energy Consumption")
st.pyplot(fig)

# -------------------------------
# Function to create PDF report
# -------------------------------
def create_pdf():
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)
    width, height = A4

    # Title
    c.setFont("Helvetica-Bold", 18)
    c.drawCentredString(width/2, height-100, "Smart Energy Meter Project Report")

    # Project description
    c.setFont("Helvetica", 12)
    text = c.beginText(50, height-150)
    lines = [
        "This project demonstrates the concept of a Smart Energy Meter.",
        "It helps in monitoring electricity usage efficiently and provides",
        "data visualization for better understanding of consumption patterns.",
        "",
        "The system is developed using Python and Streamlit.",
        "It showcases simulated weekly energy usage data and visualization.",
        "",
        "Key Features:",
        " - Display of energy usage in tabular format",
        " - Visualization of data using charts",
        " - Option to download project report in PDF",
        "",
        "",
        "------------------------------------------",
        "Special Thanks 🙏",
        "This project has been successfully completed",
        "under the constant motivation and guidance of",
        "Dr. Vijayraj (Asst. Prof, AI&DS Dept).",
        "His encouragement and support were invaluable.",
        "------------------------------------------"
    ]
    for line in lines:
        text.textLine(line)
    c.drawText(text)

    c.showPage()
    c.save()
    buffer.seek(0)
    return buffer

# -------------------------------
# Download Button
# -------------------------------
st.subheader("📥 Download Project Report")
pdf_buffer = create_pdf()
st.download_button(
    label="Download Report as PDF",
    data=pdf_buffer,
    file_name="Smart_Energy_Meter_Report.pdf",
    mime="application/pdf"
)

# -------------------------------
# Footer
# -------------------------------
st.markdown(
    """
    ---
    ✅ Project done individually by **Darshan JR**  
    🌟 With constant motivation from **Dr. Vijayraj (Asst. Prof, AI&DS Dept)**
    """
)
