from decouple import config


class Settings:
    MONGO_URI: str = config("MONGO_URI", default="mongodb://localhost:27017")
    MONGO_DB: str = config("MONGO_DB", default="fastapi_project")
    JWT_SECRET_KEY: str = config("JWT_SECRET_KEY", default="your_secret_key")
    JWT_ALGORITHM: str = config("JWT_ALGORITHM", default="HS256")
    JWT_EXPIRATION_MINUTES: int = config("JWT_EXPIRATION_MINUTES", cast=int, default=60)


settings = Settings()
