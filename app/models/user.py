from pydantic import BaseModel, EmailStr
from bson import ObjectId
from typing import Optional


class UserModel(BaseModel):
    id: Optional[ObjectId]
    user_name: str
    password: str
    phone: str
