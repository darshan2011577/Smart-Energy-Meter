import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import warnings

# Ignore sklearn warnings
warnings.filterwarnings("ignore", category=UserWarning)

# 🔹 Step 1: Generate Dummy Energy Data (30 days)
def generate_energy_data(filename="energy_data.csv"):
    np.random.seed(42)
    days = np.arange(1, 31)  # 30 days
    usage = 5 + 2 * np.sin(days / 3) + np.random.normal(0, 0.3, size=30)  # kWh
    data = pd.DataFrame({"Day": days, "Usage_kWh": usage})
    data.to_csv(filename, index=False)
    print("✅ Energy data saved to", filename)
    return data

# 🔹 Step 2: Train Model & Predict Future Usage
def train_and_predict(filename="energy_data.csv", future_days=7):
    data = pd.read_csv(filename)
    X = data[["Day"]]
    y = data["Usage_kWh"]

    model = LinearRegression()
    model.fit(X, y)

    # Predict future usage
    future_X = np.arange(31, 31 + future_days).reshape(-1, 1)
    predicted_usage = model.predict(future_X)

    return data, future_X, predicted_usage

# 🔹 Step 3: Check Alerts
def check_alerts(predicted_usage, threshold=8):
    alerts = []
    for i, usage in enumerate(predicted_usage, start=31):
        if usage > threshold:
            alerts.append(f"⚠️ High usage alert on Day {i}: {usage:.2f} kWh")
    if not alerts:
        alerts.append("✅ No unusual consumption detected.")
    return alerts

# 🔹 Step 4: Visualization
def plot_usage_and_cost(data, future_X, predicted_usage, daily_bills):
    plt.figure(figsize=(12, 6))

    # --- Line Chart (Energy Usage) ---
    plt.subplot(1, 2, 1)
    plt.plot(data["Day"], data["Usage_kWh"], label="Actual Usage (Past 30 days)", marker="o")
    plt.plot(future_X, predicted_usage, label="Predicted Usage (Next 7 days)", marker="x", linestyle="--")
    plt.xlabel("Day")
    plt.ylabel("Energy Usage (kWh)")
    plt.title("Smart Energy Meter - Usage Prediction")
    plt.legend()
    plt.grid(True)

    # --- Bar Chart (Daily Cost) ---
    plt.subplot(1, 2, 2)
    days = np.arange(31, 31 + len(daily_bills))
    plt.bar(days, daily_bills, color="orange", alpha=0.8)
    plt.xlabel("Day")
    plt.ylabel("Cost (₹)")
    plt.title("Predicted Daily Cost")
    plt.grid(axis="y")

    plt.tight_layout()
    plt.show()

# 🔹 Step 5: Main Program
if __name__ == "__main__":
    print("🔄 Generating data...")
    data = generate_energy_data()

    print("\n🤖 Training model & predicting future usage...")
    data, future_X, predicted_usage = train_and_predict()

    # Billing Calculation
    rate_per_kWh = 6.5  # ₹6.5 per unit
    daily_bills = predicted_usage * rate_per_kWh
    total_bill = daily_bills.sum()

    print("\n📊 Predicted Usage & Daily Bill for Next 7 Days:")
    for i, (usage, bill) in enumerate(zip(predicted_usage, daily_bills), start=31):
        print(f"Day {i}: {usage:.2f} kWh → ₹{bill:.2f}")

    print(f"\n💰 Estimated Total Bill for Next 7 Days: ₹{total_bill:.2f}")

    print("\n🚨 Checking alerts...")
    alerts = check_alerts(predicted_usage)
    for alert in alerts:
        print(alert)

    # Show Visualization
    plot_usage_and_cost(data, future_X, predicted_usage, daily_bills)
