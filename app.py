# app.py

from fastapi import FastAPI
from utils.check_expiry import check_expiry_dates  # KEEP this import because your Render expects it

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the SaveStock API!"}

@app.post("/check-expiry/")
async def check_expiry(file: UploadFile = File(...)):
    results = await check_expiry_dates(file)
    return results
