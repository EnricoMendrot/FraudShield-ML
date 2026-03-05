from fastapi import APIRouter, Depends, HTTPException
from api.models import User
from sqlalchemy.orm import sessionmaker, Session
from api.dependencies import get_session
from api.utils import hash_password, verify_password
from api.schemas import UserSchema

auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.post("/login")
async def login():
    """
    Authenticate user and return access token.
    """
    return {"message": "Login successful."}

@auth_router.post("/register")
async def register(userschema: UserSchema, session: Session = Depends(get_session)):
    """
    Register a new user account.
    """
    user = session.query(User).filter(User.email == userschema.email).first()
    if user:
        raise HTTPException(status_code=400, detail="User already exists.")
    else:
        new_user = User(email=userschema.email, 
                        hashed_password=hash_password(userschema.password), 
                        username=userschema.username,
                        is_active=userschema.is_active,
                        is_admin=userschema.is_admin)
        session.add(new_user)
        session.commit()
        return {"message": f"Registration successful {userschema.username}."}
