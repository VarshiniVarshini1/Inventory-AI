from sqlalchemy import Column, Integer, String, Float, Boolean, Date
from database import Base

class Inventory(Base):
    __tablename__ = "inventory"

    id = Column(Integer, primary_key=True)
    sku = Column(String)
    product_name = Column(String)
    quantity = Column(Integer)
    reorder_level = Column(Integer)
    safety_stock = Column(Integer)
    price = Column(Float)
    expiry_date = Column(Date)
    supplier_id = Column(Integer)

class Supplier(Base):
    __tablename__ = "suppliers"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    rating = Column(Float)
    delivery_speed = Column(Float)
    defect_rate = Column(Float)
    cost_score = Column(Float)

class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    role = Column(String)
