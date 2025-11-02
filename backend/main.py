from fastapi import FastAPI,Depends, HTTPException
from sqlalchemy import Select
import uvicorn
from core.database import engine
import models
from typing import Annotated
from sqlalchemy.orm import Session
from core.database import getDB
from sqlalchemy.ext.asyncio import AsyncSession
from api.user_router import router as user_router
from api.weather_router import router as weather_router
app=FastAPI()

# metadata stores all information about  models,
# create_all() tells SQLAlchemy: create all tables in the database that are defined in Base.metadata.
# bind=engine -> specifies which database to use (PostgreSQL).
app.include_router(user_router)
app.include_router(weather_router)

async def startup():
    
    async with engine.begin() as conn:
        await conn.run_sync(models.Base.metadata.create_all)
    
# @app.post('/create-user')
# async def createUser(name: str, email: str, db: AsyncSession = Depends(getDB)):
#     result= await db.execute(Select(models.User).where(models.User.email==email))
#     existing_user = result.scalar_one_or_none()
#     if existing_user:
#         raise HTTPException(status_code=400, detail="User already exists")
#     new_user = models.User(name=name, email=email)
#     db.add(new_user)
#     await db.commit()
#     await db.refresh(new_user)
#     return {"message": "User created successfully", "user": {"id": new_user.id, "name": new_user.name}}

# @app.get("/get-users")
# async def getUser(db: AsyncSession = Depends(getDB)):
#     result = await db.execute(Select(models.User))
#     users = result.scalars().all()
#     return users

# @app.put("/update-user")
# async def update_user(userId: int, email: str, db: AsyncSession = Depends(getDB)):
#     # 1️⃣ Find the user by ID
#     result = await db.execute(Select(models.User).where(models.User.id == userId))
#     user = result.scalar_one_or_none()

#     if not user:
#         return {"error": "User not found"}
#     user.email = email
#     await db.commit()
#     await db.refresh(user)
#     return {"message": "User updated successfully", "user": {"id": user.id, "email": user.email}}

    
    
    

