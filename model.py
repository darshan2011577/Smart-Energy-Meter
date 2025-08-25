import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

def train_and_predict():
    # Load past energy usage data
    data = pd.read_csv("energy_data.csv")
    X = data[["Day"]]
    y = data["Usage_kWh"]

    # Train model
    model = LinearRegression()
    model.fit(X, y)

    # Predict next 7 days usage
    future_days = np.arange(len(data)+1, len(data)+8).reshape(-1, 1)
    future_usage = model.predict(pd.DataFrame(future_days, columns=["Day"]))

    # Show predictions
    print("\n📊 Predicted Usage for Next 7 Days:")
    for d, u in zip(range(len(data)+1, len(data)+8), future_usage):
        print(f"Day {d}: {u:.2f} kWh")

    # -----------------------------
    # Step: Bill Calculation
    # -----------------------------
    rate_per_kWh = 6.5  # Example: ₹6.5 per kWh
    predicted_bill = np.sum(future_usage) * rate_per_kWh
    print(f"\n💰 Estimated Bill for Next 7 Days: ₹{predicted_bill:.2f}")

    # Plot actual vs predicted usage
    plt.plot(data["Day"], data["Usage_kWh"], label="Actual Usage")
    plt.plot(future_days, future_usage, 'r--', label="Predicted Usage")
    plt.xlabel("Day")
    plt.ylabel("Usage (kWh)")
    plt.title("Energy Usage Prediction")
    plt.legend()
    plt.show()

    return future_usage

# Run this file directly for testing
if __name__ == "__main__":
    train_and_predict()
def train_and_predict():
    # Load past energy usage data
    data = pd.read_csv("energy_data.csv")
    X = data[["Day"]]
    y = data["Usage_kWh"]

    # Train model
    model = LinearRegression()
    model.fit(X, y)

    # Predict next 7 days usage
    future_days = np.arange(len(data)+1, len(data)+8).reshape(-1, 1)
    future_usage = model.predict(pd.DataFrame(future_days, columns=["Day"]))

    # Show predictions
    print("\n📊 Predicted Usage for Next 7 Days:")
    rate_per_kWh = 6.5  # Example: ₹6.5 per unit
    daily_bills = []

    for d, u in zip(range(len(data)+1, len(data)+8), future_usage):
        cost = u * rate_per_kWh
        daily_bills.append(cost)
        print(f"Day {d}: {u:.2f} kWh → ₹{cost:.2f}")

    # -----------------------------
    # Step: Bill Calculation
    # -----------------------------
    predicted_bill = np.sum(daily_bills)
    print(f"\n💰 Estimated Total Bill for Next 7 Days: ₹{predicted_bill:.2f}")

    # Plot actual vs predicted usage
    plt.plot(data["Day"], data["Usage_kWh"], label="Actual Usage")
    plt.plot(future_days, future_usage, 'r--', label="Predicted Usage")
    plt.xlabel("Day")
    plt.ylabel("Usage (kWh)")
    plt.title("Energy Usage Prediction")
    plt.legend()
    plt.show()

    return future_usage
    
