import pandas as pd
import numpy as np

def generate_energy_data(days=30):
    np.random.seed(42)
    usage = 5 + np.random.rand(days) * 5   # 5–10 kWh/day
    data = pd.DataFrame({
        "Day": np.arange(1, days + 1),
        "Usage_kWh": usage
    })
    data.to_csv("energy_data.csv", index=False)
    print("✅ Energy data saved to energy_data.csv")

if __name__ == "__main__":
    generate_energy_data()
