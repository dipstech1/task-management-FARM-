import bcrypt
from datetime import datetime, timedelta, timezone
from jose import jwt
from app.core.config import settings


def generate_salt(rounds = 10):
    return bcrypt.gensalt(rounds=rounds) 

def hash_data(data:str):
    data_bytes = data.encode()
    return bcrypt.hashpw(data_bytes,generate_salt()).decode()

def decode_data(encoded_data : str, original_data : str):
    encoded_data_bytes = encoded_data.encode()
    original_data_bytes = original_data.encode()

    return bcrypt.checkpw(original_data_bytes, encoded_data_bytes)

def create_jwt(data:dict, expiry_time :int | None = None):
    encode_data = data.copy()
    expire_min = timedelta(minutes=expiry_time) if expiry_time else timedelta(minutes=15)
    expire = datetime.now(timezone.utc) + expire_min
    encode_data.update({'expires' : int(expire.timestamp())})
    token = jwt.encode(claims=encode_data, key=settings.JWT_SECRET, algorithm=settings.JWT_ALGORITHM)
    return token
    