import pandas as pd

def zscore_anomaly(series, threshold=2):
    """
    Detect anomalies using Z-score method.
    series: Pandas Series (e.g., energy consumption data)
    threshold: Z-score value above which anomaly is flagged
    """
    mean = series.mean()
    std = series.std()
    z_scores = (series - mean) / std
    anomalies = series[z_scores.abs() > threshold]
    return anomalies
