from fastapi import APIRouter, Depends
from core.database import getDB
from sqlalchemy.ext.asyncio import AsyncSession
from services import weather_service
from datetime import datetime
router = APIRouter(prefix='/weather',tags=["Weather"])
@router.get('/city')
async def fetch_Weather_By_City(city: str):
    return await weather_service.fetch_Weather_By_City(city)
@router.get('/summary/city')
async def getSummary(city:str):
    return await weather_service.getWeatherSummary(city)
    

@router.get('/city/by_date')
async def get_weather_by_date(city:str,target_date:datetime):
    return await weather_service.get_weather_by_date(city,target_date)
    
    
    