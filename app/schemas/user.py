from pydantic import BaseModel


class UserCreateSchema(BaseModel):
    user_name: str
    password: str
    phone: str


class UserLoginSchema(BaseModel):
    user_name: str
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
