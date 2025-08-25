# anomaly.py
import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest

def zscore_anomaly(series, window=7, thresh=2.5):
    roll_mean = series.rolling(window).mean()
    roll_std = series.rolling(window).std().replace(0,1e-6)
    z = (series - roll_mean)/roll_std
    return z.abs() > thresh

def iforest_anomaly(series):
    model = IsolationForest(contamination=0.02, random_state=42)
    model.fit(series.values.reshape(-1,1))
    pred = model.predict(series.values.reshape(-1,1))
    # -1 => anomaly
    return pred == -1
