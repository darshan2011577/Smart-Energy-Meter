# lstm_model.py
import numpy as np, pandas as pd
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from sklearn.preprocessing import MinMaxScaler

def series_to_supervised(series, n_in=7):
    X, y = [], []
    for i in range(len(series) - n_in):
        X.append(series[i:i+n_in])
        y.append(series[i+n_in])
    return np.array(X), np.array(y)

def train_lstm(csvfile='energy_data.csv', n_in=7, epochs=30, batch=16):
    df = pd.read_csv(csvfile)
    series = df['Usage_kWh'].values.reshape(-1,1)
    scaler = MinMaxScaler()
    series_s = scaler.fit_transform(series)
    X, y = series_to_supervised(series_s.flatten(), n_in=n_in)
    X = X.reshape((X.shape[0], X.shape[1], 1))
    model = Sequential([LSTM(64, input_shape=(n_in,1)), Dense(1)])
    model.compile(optimizer='adam', loss='mse')
    model.fit(X, y, epochs=epochs, batch_size=batch, verbose=1)
    return model, scaler

def predict_future(model, scaler, recent_series, n_in=7, future_steps=7):
    preds = []
    seq = recent_series[-n_in:].copy()
    for _ in range(future_steps):
        inp = scaler.transform(seq.reshape(-1,1)).reshape(1,n_in,1)
        p = model.predict(inp)[0,0]
        preds.append(p)
        # inverse scale for next step input
        seq = np.append(seq[1:], scaler.inverse_transform([[p]])[0,0])
    # final preds are scaled->inverse
    preds_inv = scaler.inverse_transform(np.array(preds).reshape(-1,1)).flatten()
    return preds_inv
