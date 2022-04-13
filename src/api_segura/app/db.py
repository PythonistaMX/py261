from typing import AsyncGenerator
from fastapi_users.db import SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from config import SQLALCHEMY_DATABASE_URL
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi import Depends
from app.models import Base, UserDB, UserTable

engine = create_engine(SQLALCHEMY_DATABASE_URL)
async_engine = create_async_engine(SQLALCHEMY_DATABASE_URL)

async_session_maker = sessionmaker(async_engine, class_=AsyncSession, expire_on_commit=False)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

async def create_db_and_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(UserDB, session, UserTable)
