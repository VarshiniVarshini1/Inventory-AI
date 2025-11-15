from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from utils.jwt_handler import create_jwt_token, verify_password
from models import Users
from database import get_db

router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post("/signup")
def signup(user: dict, db: Session = Depends(get_db)):
    new_user = Users(username=user["username"], password=user["password"], role=user["role"])
    db.add(new_user)
    db.commit()
    return {"message": "User registered"}

@router.post("/login")
def login(user: dict, db: Session = Depends(get_db)):
    db_user = db.query(Users).filter(Users.username == user["username"]).first()
    if not db_user or not verify_password(user["password"], db_user.password):
        return {"error": "Invalid credentials"}

    token = create_jwt_token({"user": db_user.username, "role": db_user.role})
    return {"access_token": token}
