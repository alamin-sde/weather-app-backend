from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.user_schema import UserCreate
from services.user_service import createUser
from core.database import getDB
# from schemas.user_schema import UserCreate, UserResponse
# from services.user_service import create_new_user
router = APIRouter(prefix="/users",tags=["Users"])
@router.post("/register")
async def registerUser(user: UserCreate, db: AsyncSession = Depends(getDB)):
    return await createUser(user,db)
    