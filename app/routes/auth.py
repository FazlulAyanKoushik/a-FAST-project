from fastapi import APIRouter, HTTPException, Depends
from app.schemas.user import UserCreateSchema, UserLoginSchema, TokenResponse
from app.core.db import get_db
from app.core.config import settings
from passlib.hash import bcrypt
import jwt as pyjwt
from datetime import datetime, timedelta, timezone
router = APIRouter()


@router.post("/register", response_model=dict)
async def register_user(user: UserCreateSchema):
    db = get_db()
    existing_user = await db.users.find_one({"user_name": user.user_name})
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists")

    hashed_password = bcrypt.hash(user.password)
    user_data = user.dict()
    user_data["password"] = hashed_password

    await db.users.insert_one(user_data)
    return {"message": "User registered successfully"}


@router.post("/login", response_model=TokenResponse)
async def login_user(user: UserLoginSchema):
    db = get_db()
    db_user = await db.users.find_one({"user_name": user.user_name})
    if not db_user or not bcrypt.verify(user.password, db_user["password"]):
        raise HTTPException(status_code=400, detail="Invalid username or password")

    token_payload = {
        "user_name": db_user["user_name"],
        "exp": datetime.now(timezone.utc)
        + timedelta(minutes=settings.JWT_EXPIRATION_MINUTES),
    }

    token = pyjwt.encode(
        token_payload,
        settings.JWT_SECRET_KEY,
        algorithm=settings.JWT_ALGORITHM,
    )

    return TokenResponse(access_token=token)
