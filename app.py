from fastapi import FastAPI, UploadFile, File
from utils.expiry_checker import check_expiry_dates

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the SaveStock API!"}

@app.post("/check-expiry/")
async def check_expiry(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        temp_file_path = f"/tmp/{file.filename}"

        with open(temp_file_path, "wb") as f:
            f.write(contents)

        expired, near_expiry, offer_products = check_expiry_dates(temp_file_path)

        return {
            "expired_products": expired,
            "near_expiry_products": near_expiry,
            "offer_products": offer_products
        }

    except Exception as e:
        return {"error": str(e)}
