import pandas as pd
from models import Inventory
from sqlalchemy.orm import Session

def generate_inventory_report(db: Session):
    data = db.query(Inventory).all()
    records = []

    for item in data:
        records.append({
            "SKU": item.sku,
            "Product Name": item.product_name,
            "Quantity": item.quantity,
            "Reorder Level": item.reorder_level,
            "Safety Stock": item.safety_stock,
            "Supplier ID": item.supplier_id
        })

    df = pd.DataFrame(records)
    df.to_excel("inventory_report.xlsx", index=False)
    return "inventory_report.xlsx"
