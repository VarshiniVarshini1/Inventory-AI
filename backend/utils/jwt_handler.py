import jwt
import config
from datetime import datetime, timedelta

def create_jwt_token(data: dict):
    expire = datetime.utcnow() + timedelta(days=1)
    data.update({"exp": expire})
    return jwt.encode(data, config.JWT_SECRET, algorithm=config.JWT_ALGORITHM)

def verify_jwt_token(token: str):
    try:
        return jwt.decode(token, config.JWT_SECRET, algorithms=[config.JWT_ALGORITHM])
    except:
        return None

def verify_password(input_password: str, stored_password: str):
    return input_password == stored_password  # Simple match (update with hashing later)
