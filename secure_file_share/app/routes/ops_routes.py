from fastapi import APIRouter, UploadFile, File, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from starlette.status import HTTP_403_FORBIDDEN
from app.auth.auth_handler import decode_access_token
import os
import shutil

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/client/login")  # reuse token path

UPLOAD_DIR = "uploaded_files"
os.makedirs(UPLOAD_DIR, exist_ok=True)

def get_current_user(token: str = Depends(oauth2_scheme)):
    payload = decode_access_token(token)
    if payload is None:
        raise HTTPException(status_code=HTTP_403_FORBIDDEN, detail="Invalid token")
    return payload

@router.post("/upload")
def upload_file(file: UploadFile = File(...), user=Depends(get_current_user)):
    if user.get("role") != "ops":
        raise HTTPException(status_code=403, detail="Only ops users can upload")

    allowed_ext = (".pptx", ".docx", ".xlsx")
    filename = file.filename.lower()
    if not filename.endswith(allowed_ext):
        raise HTTPException(status_code=400, detail="Invalid file type")

    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {"message": "File uploaded successfully", "filename": file.filename}
