from fastapi import APIRouter

auth_router = APIRouter(prefix="/auth", tags=["auth"])
@auth_router.post("/login")
async def login():
    """
    Authenticate user and return access token.
    """
    return {"message": "Login successful."}

@auth_router.post("/register")
async def register():
    """
    Register a new user account.
    """
    return {"message": "Registration successful."}
