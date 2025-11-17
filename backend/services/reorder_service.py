from models import Inventory
from sqlalchemy.orm import Session

def calculate_reorder_levels(db: Session):
    items = db.query(Inventory).all()

    for item in items:
        daily_usage = max(item.quantity / 30, 1)
        lead_time = 7  # default lead time
        safety_stock = round(daily_usage * 5)
        reorder_level = round(daily_usage * lead_time + safety_stock)

        item.safety_stock = safety_stock
        item.reorder_level = reorder_level

    db.commit()
