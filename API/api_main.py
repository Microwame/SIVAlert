from fastapi import FastAPI, HTTPException, Request, UploadFile, File

app = FastAPI()

@app.post("/image-upload")
def file_upload(file: UploadFile = File(...)):
    if Request.method != "POST":  # Verifica se o método da requisição é POST
        raise HTTPException(
            status_code=405,
            detail="This endpoint only supports POST requests."
        )
    if not file:                    # Verifica se o arquivo foi enviado
        raise HTTPException(
            status_code=400,
            detail="No file uploaded."
        )
    if file.content_type not in ["image/jpeg", "image/png"]: # Verifica se o tipo de arquivo é JPEG ou PNG
        raise HTTPException(
            status_code=415,
            detail="Invalid file type. Only JPEG and PNG are allowed."
        )
    if file.size is not None and file.size > 5 * 1024 * 1024:               # Limite 5 Megabytes
        raise HTTPException(
            status_code=413,
            detail="File size exceeds the limit of 5 MB."
        )
    # Ollama aqui
    del file
    return {"message": "File uploaded successfully."}