from fastapi import APIRouter, HTTPException, Depends, Form
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from app.auth.auth_handler import hash_password, verify_password, create_access_token, decode_access_token
import uuid

router = APIRouter()

# In-memory DB (for now)
users = {}
files = {}

@router.post("/signup")
def signup(username: str = Form(...), password: str = Form(...)):
    if username in users:
        raise HTTPException(status_code=400, detail="User already exists")
    
    token = str(uuid.uuid4())
    users[username] = {
        "username": username,
        "password": hash_password(password),
        "role": "client",
        "verified": False,
        "token": token,
    }

    verify_url = f"http://localhost:8000/client/verify-email?token={token}"
    return {"message": "Signed up successfully", "verify_url": verify_url}

@router.get("/verify-email")
def verify_email(token: str):
    for user in users.values():
        if user["token"] == token:
            user["verified"] = True
            return {"message": "Email verified successfully"}
    raise HTTPException(status_code=400, detail="Invalid token")

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = users.get(form_data.username)
    if not user or not verify_password(form_data.password, user["password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    if not user["verified"]:
        raise HTTPException(status_code=401, detail="Email not verified")

    access_token = create_access_token({"sub": user["username"], "role": user["role"]})
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/files")
def list_files(token: str = Depends(OAuth2PasswordBearer(tokenUrl="/client/login"))):
    payload = decode_access_token(token)
    if payload["role"] != "client":
        raise HTTPException(status_code=403, detail="Not allowed")
    file_list = os.listdir("uploaded_files")
    return {"files": file_list}

@router.get("/download-file/{filename}")
def generate_download_link(filename: str, token: str = Depends(OAuth2PasswordBearer(tokenUrl="/client/login"))):
    payload = decode_access_token(token)
    if payload["role"] != "client":
        raise HTTPException(status_code=403, detail="Only client users allowed")

    encrypted_link = str(uuid.uuid4())  # Simulated secure link
    files[encrypted_link] = filename
    return {"download-link": f"http://localhost:8000/client/download/{encrypted_link}", "message": "success"}

@router.get("/download/{secure_id}")
def download_file(secure_id: str, token: str = Depends(OAuth2PasswordBearer(tokenUrl="/client/login"))):
    payload = decode_access_token(token)
    if payload["role"] != "client":
        raise HTTPException(status_code=403, detail="Only client users allowed")
    
    filename = files.get(secure_id)
    if not filename:
        raise HTTPException(status_code=404, detail="Invalid or expired link")

    file_path = os.path.join("uploaded_files", filename)
    return {"message": f"File ready to download (simulated): {file_path}"}
