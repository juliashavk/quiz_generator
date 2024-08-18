from fastapi import UploadFile
async def process_pdf(file: UploadFile):
    # Read the file
    content = await file.read()

    # Implement your PDF processing logic here
    # This could involve parsing the PDF and extracting questions

    # For demonstration purposes, let's return a mock list of questions
    return ["Question 1", "Question 2", "Question 3"]