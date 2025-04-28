# app.py

from fastapi import FastAPI
from routers import expiry_router

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the SaveStock API!"}

# Include the expiry checking routes
app.include_router(expiry_router.router, prefix="/expiry", tags=["Expiry Checker"])
