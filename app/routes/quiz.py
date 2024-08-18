from fastapi import APIRouter

router = APIRouter()

@router.post("/upload-pdf/")
async def upload_pdf():
    return {"message": "PDF uploaded"}

