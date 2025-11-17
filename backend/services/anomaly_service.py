from models import Inventory
from sqlalchemy.orm import Session

def detect_anomalies(db: Session):
    anomalies = []
    items = db.query(Inventory).all()

    for item in items:
        if item.quantity <= item.safety_stock / 2:
            anomalies.append({
                "sku": item.sku,
                "issue": "Stock critically low"
            })
        if item.expiry_date:
            anomalies.append({
                "sku": item.sku,
                "issue": "Expiry approaching"
            })

    return anomalies
