from fastapi import FastAPI
from app.routes import auth
from app.core.db import init_db

app = FastAPI()

# Initialize MongoDB
@app.on_event("startup")
async def startup_event():
    await init_db()

# Include routes
app.include_router(auth.router)
