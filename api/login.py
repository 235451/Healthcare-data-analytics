"""
Login endpoint
"""

from fastapi import APIRouter, Form, HTTPException
from api.auth import authenticate_user, create_access_token

router = APIRouter()

@router.post("/login")
def login(username: str = Form(...), password: str = Form(...)):
    user = authenticate_user(username, password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({
        "sub": user["username"],
        "role": user["role"]
    })

    return {
        "access_token": token,
        "token_type": "bearer",
        "role": user["role"]
    }
