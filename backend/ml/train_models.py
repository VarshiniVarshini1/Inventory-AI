import pandas as pd
import joblib
from prophet import Prophet
from sklearn.model_selection import train_test_split
import xgboost as xgb
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from statsmodels.tsa.arima.model import ARIMA
import numpy as np
import os

# Load training data
df = pd.read_csv("ml/data/sample_sales.csv")
df = df.rename(columns={"date": "ds", "sales": "y"})

# --------------------------
# 1. Prophet Model
# --------------------------
print("Training Prophet model...")
prophet_model = Prophet()
prophet_model.fit(df)
joblib.dump(prophet_model, "ml/prophet_model.pkl")
print("Prophet saved.")

# --------------------------
# 2. XGBoost Model
# --------------------------
print("Training XGBoost model...")
df["day"] = np.arange(len(df))

X = df["day"].values.reshape(-1, 1)
y = df["y"].values

model_xgb = xgb.XGBRegressor()
model_xgb.fit(X, y)
model_xgb.save_model("ml/xgb_model.json")
print("XGBoost saved.")

# --------------------------
# 3. LSTM Model
# --------------------------
print("Training LSTM model...")
values = df["y"].values
sequence = []

window = 10
for i in range(len(values) - window):
    sequence.append(values[i:i+window+1])

sequence = np.array(sequence)
X_lstm, y_lstm = sequence[:, :-1], sequence[:, -1]
X_lstm = X_lstm.reshape((X_lstm.shape[0], X_lstm.shape[1], 1))

lstm_model = Sequential()
lstm_model.add(LSTM(50, activation="relu", input_shape=(window, 1)))
lstm_model.add(Dense(1))
lstm_model.compile(optimizer="adam", loss="mse")
lstm_model.fit(X_lstm, y_lstm, epochs=10, verbose=1)

lstm_model.save("ml/lstm_model.h5")
print("LSTM saved.")

# --------------------------
# 4. ARIMA Model
# --------------------------
print("Training ARIMA model...")
arima = ARIMA(df["y"], order=(5,1,0))
arima_model = arima.fit()
joblib.dump(arima_model, "ml/arima_model.pkl")
print("ARIMA saved.")

print("\n🎉 ALL MODELS TRAINED & SAVED SUCCESSFULLY!")
