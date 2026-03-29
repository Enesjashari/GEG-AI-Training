"""User Pydantic schemas."""
from typing import Optional

from pydantic import BaseModel, EmailStr, Field

from src.backend_template.core.config import settings


class UserBase(BaseModel):
    email: EmailStr


class UserCreate(UserBase):
    password: str = Field(min_length=8, description="Min 8 chars")


class UserUpdate(BaseModel):
    email: Optional[EmailStr] = None
    is_active: Optional[bool] = None
    password: Optional[str] = Field(None, min_length=8)


class User(UserBase):
    id: int
    is_active: bool
    created_at: str

    model_config = {
        "from_attributes": True,
    }


class UserInDB(User):
    hashed_password: str

