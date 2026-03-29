"""API v1 users endpoints."""
from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from slowapi import Limiter
from slowapi.util import get_remote_address

from src.backend_template.core.security import create_access_token, get_current_user, Token
from src.backend_template.crud.user import (
    authenticate,
    create,
    delete,
    get,
    get_multi,
    update,
)
from src.backend_template.db.session import AsyncDBSession
from src.backend_template.models.user import User
from src.backend_template.schemas.user import User, UserCreate, UserUpdate
from src.backend_template.core.config import settings

router = APIRouter()

limiter = Limiter(key_func=get_remote_address)


@router.post("/users/", response_model=User, status_code=status.HTTP_201_CREATED)
@limiter.limit("5/minute")
async def create_user(user_in: UserCreate, session: AsyncDBSession):
    """Create new user."""
    db_user = await get_by_email(session, email=user_in.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return await create(session, user_in)


@router.get("/users/", response_model=List[User])
async def list_users(
    session: AsyncDBSession,
    skip: int = 0,
    limit: int = 100,
    current_user: str = Depends(get_current_user),
):
    """List users (admin only)."""
    # TODO: role check
    return await get_multi(session, skip=skip, limit=limit)


@router.get("/users/{user_id}", response_model=User)
async def read_user(user_id: int, session: AsyncDBSession):
    """Get user by ID."""
    user = await get(session, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.put("/users/{user_id}", response_model=User)
async def update_user(
    user_id: int,
    user_in: UserUpdate,
    session: AsyncDBSession,
    current_user: str = Depends(get_current_user),
):
    """Update user."""
    user = await get(session, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    updated_user = await update(session, user, user_in)
    if not updated_user:
        raise HTTPException(status_code=400, detail="Update failed")
    return updated_user


@router.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(
    user_id: int,
    session: AsyncDBSession,
    current_user: str = Depends(get_current_user),
):
    """Delete user."""
    if not await delete(session, user_id):
        raise HTTPException(status_code=404, detail="User not found")


@router.post("/login", response_model=Token)
async def login(email: str, password: str, session: AsyncDBSession):
    """Login and get token."""
    user = await authenticate(session, email, password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}

