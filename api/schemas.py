from pydantic import BaseModel
from typing import Optional

class UserSchema(BaseModel):
    username: str
    email: str
    password: str
    is_active: Optional[bool] = True
    is_admin: Optional[bool] = True

    class Config:
        from_attributes = True