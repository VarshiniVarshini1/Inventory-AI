from models import Supplier
from sqlalchemy.orm import Session

def compute_supplier_rating(db: Session):
    suppliers = db.query(Supplier).all()

    for s in suppliers:
        # Weighted score
        rating = (
            (1 - s.defect_rate) * 0.4 +
            s.delivery_speed * 0.3 +
            s.cost_score * 0.3
        ) * 10

        s.rating = round(rating, 2)

    db.commit()
