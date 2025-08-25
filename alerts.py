def check_alerts(predictions, threshold=9):
    for i, usage in enumerate(predictions, start=1):
        if usage > threshold:
            print(f"⚠️ ALERT: High usage predicted on Day {i} → {usage:.2f} kWh")

if __name__ == "__main__":
    from model import train_and_predict
    future_usage = train_and_predict()
    check_alerts(future_usage)
