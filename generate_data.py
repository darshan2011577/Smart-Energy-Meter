import pandas as pd
import numpy as np

def generate_energy_data(filename="energy_data.csv", days=30):
    np.random.seed(42)  # For reproducibility
    days_list = np.arange(1, days + 1)
    usage = 5 + np.random.normal(0, 1, days)  # Avg ~5 kWh with noise

    df = pd.DataFrame({"Day": days_list, "Usage_kWh": usage})
    df.to_csv(filename, index=False)
