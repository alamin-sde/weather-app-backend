from fastapi import HTTPException
from sqlalchemy import Select
from schemas.user_schema import UserCreate
from sqlalchemy.ext.asyncio import AsyncSession
from models.user import User
from core.security import hash_password
async def createUser(user:UserCreate,db:AsyncSession):
    try:
        result = await db.execute(Select(User).where(User.email==user.email))
        existing_user = result.scalar_one_or_none()
        if existing_user:
            raise HTTPException(status_code=400,detail="User already exists")
        hashed_password = hash_password(user.password)
        new_user = User(
            username=user.username,
            email=user.email,
            password=hashed_password,
        )
        db.add(new_user)
        await db.commit()
        return {"message":"User created successfully"}
    except Exception as e:
        await db.rollback()
        raise HTTPException(status_code=500, detail=str(e))
        
        
   
    