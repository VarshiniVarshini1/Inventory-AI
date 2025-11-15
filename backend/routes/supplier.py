from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import Supplier
from services.supplier_service import compute_supplier_rating

router = APIRouter(prefix="/supplier", tags=["Suppliers"])

@router.get("/")
def get_suppliers(db: Session = Depends(get_db)):
    return db.query(Supplier).all()

@router.post("/")
def add_supplier(supplier: dict, db: Session = Depends(get_db)):
    new_supplier = Supplier(
        name=supplier["name"],
        rating=0,
        delivery_speed=supplier["delivery_speed"],
        defect_rate=supplier["defect_rate"],
        cost_score=supplier["cost_score"]
    )
    db.add(new_supplier)
    db.commit()
    return {"message": "Supplier added"}

@router.post("/rate")
def update_ratings(db: Session = Depends(get_db)):
    compute_supplier_rating(db)
    return {"message": "Supplier ratings updated"}
