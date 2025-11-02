from fastapi import APIRouter, Depends
from core.database import getDB
from sqlalchemy.ext.asyncio import AsyncSession
from services.weather_service import fetWeatherByCity
router = APIRouter(prefix='/weather',tags=["Weather"])
@router.get('/city')
async def fetchWeatherByCity(db: AsyncSession = Depends(getDB)):
    return await fetWeatherByCity('Kolkata',db)
    
    