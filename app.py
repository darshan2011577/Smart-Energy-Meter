import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page settings for SEO
st.set_page_config(
    page_title="Darshan JR | Smart Energy Meter",
    page_icon="⚡",
    layout="wide"
)

# Google Search Console verification meta tag (replace YOUR_CODE_HERE)
st.markdown("""
<meta name="google-site-verification" content="YOUR_CODE_HERE" />
""", unsafe_allow_html=True)

# Title & subtitle
st.title("⚡ Smart Energy Meter")
st.subheader("Created by Darshan JR")

# File uploader
uploaded_file = st.file_uploader("Upload your Smart Energy CSV file", type=["csv"])

if uploaded_file is not None:
    try:
        # Read CSV
        df = pd.read_csv(uploaded_file)

        # Ensure 'consumption' column exists
        if 'consumption' not in df.columns:
            st.error("CSV file must contain a 'consumption' column.")
        else:
            st.success("✅ File uploaded successfully!")

            # Show raw data
            st.write("### 📊 Uploaded Data")
            st.dataframe(df)

            # Plot consumption graph
            st.write("### 📈 Energy Consumption Graph")
            fig, ax = plt.subplots()
            df['consumption'].plot(ax=ax, marker='o')
            ax.set_xlabel("Index")
            ax.set_ylabel("Consumption (kWh)")
            ax.set_title("Energy Consumption Over Time")
            st.pyplot(fig)

            # Show summary statistics
            st.write("### 📑 Data Summary")
            st.write(df['consumption'].describe())

    except Exception as e:
        st.error(f"Error reading file: {e}")

else:
    st.info("📥 Please upload a CSV file to get started.")
