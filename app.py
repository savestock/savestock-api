from fastapi import FastAPI, UploadFile, File
from utils.expiry_checker import process_stock_file

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to SaveStock API. Please POST a file to /uploadfile."}

@app.post("/uploadfile")
async def upload_file(file: UploadFile = File(...)):
    contents = await file.read()
    result = process_stock_file(contents)
    return result
