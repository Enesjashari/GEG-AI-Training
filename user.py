"""User CRUD."""
from typing import List, Optional, Sequence

from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession

from src.backend_template.core.logger import logger
from src.backend_template.core.security import get_password_hash, verify_password
from src.backend_template.models.user import User
from src.backend_template.schemas.user import UserCreate, UserUpdate, UserInDB


async def get(session: AsyncSession, id_: int) -> Optional[User]:
    result = await session.execute(select(User).where(User.id == id_))
    user = result.scalar_one_or_none()
    logger.debug("User fetched", user_id=id_)
    return user


async def get_by_email(session: AsyncSession, email: str) -> Optional[User]:
    result = await session.execute(select(User).where(User.email == email))
    user = result.scalar_one_or_none()
    return user


async def authenticate(
    session: AsyncSession, email: str, password: str
) -> Optional[User]:
    user = await get_by_email(session, email)
    if not user or not verify_password(password, user.hashed_password):
        logger.warning("Auth failed", email=email)
        return None
    return user


async def create(session: AsyncSession, user_in: UserCreate) -> User:
    hashed_pwd = get_password_hash(user_in.password)
    user = User(email=user_in.email, hashed_password=hashed_pwd)
    session.add(user)
    logger.info("User created", email=user_in.email)
    return user


async def update(
    session: AsyncSession, db_user: User, user_in: UserUpdate
) -> Optional[User]:
    update_data = user_in.model_dump(exclude_unset=True)
    if "password" in update_data:
        update_data["hashed_password"] = get_password_hash(update_data.pop("password"))
    result = await session.execute(
        update(User).where(User.id == db_user.id).values(**update_data).returning(User)
    )
    return result.scalar_one_or_none()


async def delete(session: AsyncSession, id_: int) -> bool:
    result = await session.execute(delete(User).where(User.id == id_))
    logger.info("User deleted", user_id=id_)
    return result.rowcount > 0


async def get_multi(session: AsyncSession, *, skip: int = 0, limit: int = 100) -> List[User]:
    result = await session.execute(select(User).offset(skip).limit(limit).order_by(User.id))
    return result.scalars().all()

