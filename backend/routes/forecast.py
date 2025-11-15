from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from services.forecasting_service import forecast_demand
from database import get_db

router = APIRouter(prefix="/forecast", tags=["Forecasting"])

@router.get("/{sku}")
def forecast_product(sku: str, db: Session = Depends(get_db)):
    forecast = forecast_demand(sku, db)
    return {"sku": sku, "forecast": forecast}
