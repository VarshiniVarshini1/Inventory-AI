import pandas as pd
import joblib
from tensorflow.keras.models import load_model
from sqlalchemy.orm import Session
from models import Inventory
import numpy as np

# Load ML Models
prophet_model = joblib.load("ml/prophet_model.pkl")
xgb_model = joblib.load("ml/xgb_model.json")
lstm_model = load_model("ml/lstm_model.h5")
arima_model = joblib.load("ml/arima_model.pkl")

def preprocess_data(db: Session, sku: str):
    data = db.query(Inventory).filter(Inventory.sku == sku).all()
    df = pd.DataFrame([{
        "date": item.expiry_date,
        "sales": item.quantity
    } for item in data])
    
    if df.empty:
        return None
    
    df = df.rename(columns={"date": "ds", "sales": "y"})
    return df

def forecast_demand(sku: str, db: Session):
    df = preprocess_data(db, sku)
    if df is None:
        return {"error": "No sales data found"}
    
    # Prophet
    future = prophet_model.make_future_dataframe(periods=30)
    prophet_pred = prophet_model.predict(future)["yhat"].values[-30:]

    # XGBoost (dummy input)
    xgb_pred = xgb_model.predict(np.arange(30).reshape(-1,1))

    # LSTM (dummy input)
    lstm_input = np.array(df['y'].values[-10:]).reshape(1,10,1)
    lstm_pred = lstm_model.predict(lstm_input)[0]

    # ARIMA
    arima_pred = arima_model.forecast(steps=30)

    # Ensemble averaging
    final_pred = (
        prophet_pred[:30] +
        xgb_pred[:30] +
        lstm_pred[:30] +
        arima_pred[:30]
    ) / 4

    return final_pred.tolist()
