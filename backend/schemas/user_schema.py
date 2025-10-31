from pydantic import BaseModel,EmailStr
from datetime import datetime
class UserBase(BaseModel):
    username:str
    email:EmailStr
class UserCreate(UserBase):
    password:str

class User(UserBase):
    id:int
    themeMode:str
    isActive:bool
    createdAt:datetime
    updatedAt:datetime
    