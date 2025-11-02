import os
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException
from httpx import AsyncClient
from dotenv import load_dotenv
from services.ml_service import get_llm_summary,get_five_days_weather_summary
from datetime import datetime
import json
import re
load_dotenv()
WEATHER_GEO = "http://api.openweathermap.org/geo/1.0/direct"
ONECALL = "https://api.openweathermap.org/data/2.5"

OPENWEATHER_API_KEY=os.getenv('OPENWEATHER_API_KEY')
def clean_llm_output(raw_output: str):
    cleaned = re.sub(r"^```json|```$", "", raw_output.strip(), flags=re.MULTILINE).strip()
    return json.loads(cleaned)

async def fetch_Weather_By_City(city:str):
    try:
        async with AsyncClient(timeout=20) as client:
            
            geo_url = f"{WEATHER_GEO}?q={city}&limit=1&appid={OPENWEATHER_API_KEY}"
            g = await client.get(geo_url)
            g.raise_for_status()
            geo = g.json()
            if not geo:
                raise ValueError(f"City not found: {city}")
            lat=geo[0]["lat"]
            lon=geo[0]["lon"]
            onecall_url = f"{ONECALL}/weather?lat={lat}&lon={lon}&appid={OPENWEATHER_API_KEY}"
            r = await client.get(onecall_url)
            r.raise_for_status()
            data = r.json()    
            return data
        
    except Exception as e:
        raise HTTPException(e)
async def getWeatherSummary(city:str):
    try:
        raw = await fetch_Weather_By_City(city) 
        data = await get_llm_summary(raw)
        return data.strip()
    except Exception as e:
        raise HTTPException(e)

async def get_weather_by_date(city:str,target_date:datetime):
    try:
        async with AsyncClient(timeout=20) as client:
            geo_url = f"{WEATHER_GEO}?q={city}&limit=1&appid={OPENWEATHER_API_KEY}"
            g = await client.get(geo_url)
            g.raise_for_status()
            geo = g.json()
            if not geo:
                raise ValueError(f"City not found: {city}")
            lat=geo[0]["lat"]
            lon=geo[0]["lon"]
            forecast_url = f"{ONECALL}/forecast?lat={lat}&lon={lon}&appid={OPENWEATHER_API_KEY}"
            r = await client.get(forecast_url)
            r.raise_for_status()
            forecast_data = r.json()
            selected_day=[]
            for day in   forecast_data.get("list"):
                day_date = datetime.fromtimestamp(day['dt']).date()
                if day_date==target_date.date():
                    selected_day.append(day)
            
            if  len(selected_day)==0:
                return {"error":f"No forecast available for {target_date}"} 
            structuredData = await get_five_days_weather_summary(selected_day,target_date)  
            return clean_llm_output(structuredData)
            # return selected_day
            
    except Exception as e:
        raise HTTPException(e)

    
    
    
        
        
    