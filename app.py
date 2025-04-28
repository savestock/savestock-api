from fastapi import FastAPI, Request
from utils.expiry_checker import check_expiry_dates

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the SaveStock API!"}

@app.post("/check-expiry")
async def check_expiry(request: Request):
    data = await request.json()
    items = data.get("items", [])
    result = check_expiry_dates(items)
    return {"result": result}
