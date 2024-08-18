from fastapi import FastAPI, File, UploadFile
from app.utils import process_pdf

app = FastAPI()

@app.post("/upload-pdf/")
async def upload_pdf(file: UploadFile = File(...)):
    questions = await process_pdf(file)
    return {"questions": questions}
