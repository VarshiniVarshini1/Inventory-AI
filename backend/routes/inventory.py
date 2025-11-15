from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import Inventory
from services.reorder_service import calculate_reorder_levels

router = APIRouter(prefix="/inventory", tags=["Inventory"])

@router.get("/")
def get_inventory(db: Session = Depends(get_db)):
    return db.query(Inventory).all()

@router.post("/")
def add_item(item: dict, db: Session = Depends(get_db)):
    new_item = Inventory(
        sku=item["sku"],
        product_name=item["product_name"],
        quantity=item["quantity"],
        reorder_level=item.get("reorder_level", 0),
        safety_stock=item.get("safety_stock", 0),
        price=item["price"],
        expiry_date=item.get("expiry_date"),
        supplier_id=item["supplier_id"]
    )
    db.add(new_item)
    db.commit()
    return {"message": "Item added successfully"}

@router.post("/recalculate")
def recalc_levels(db: Session = Depends(get_db)):
    calculate_reorder_levels(db)
    return {"message": "Reorder levels updated"}
