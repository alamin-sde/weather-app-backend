import os
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException
from httpx import AsyncClient
from dotenv import load_dotenv
load_dotenv()
WEATHER_GEO = "http://api.openweathermap.org/geo/1.0/direct"
ONECALL = "https://api.openweathermap.org/data/2.5/weather"
OPENWEATHER_API_KEY=os.getenv('OPENWEATHER_API_KEY')
async def fetWeatherByCity(city:str,db:AsyncSession):
    try:
        async with AsyncClient(timeout=20) as client:
            
            # geo_url = f"{WEATHER_GEO}?q={city}&limit=1&appid={OPENWEATHER_API_KEY}"
            # g = await client.get(geo_url)
            # g.raise_for_status()
            # geo = g.json()
            # if not geo:
            #     raise ValueError(f"City not found: {city}")
            # lat=geo[0]["lat"]
            # lon=geo[0]["lon"]
            # onecall_url = f"{ONECALL}?lat={lat}&lon={lon}&appid={OPENWEATHER_API_KEY}"
            # r = await client.get(onecall_url)
            # r.raise_for_status()
            # data = r.json()
            data={
            "coord": {
                "lon": 88.3577,
                "lat": 22.5414
            },
            "weather": [
                {
                "id": 721,
                "main": "Haze",
                "description": "haze",
                "icon": "50d"
                }
            ],
            "base": "stations",
            "main": {
                "temp": 300.11,
                "feels_like": 302.27,
                "temp_min": 300.11,
                "temp_max": 300.11,
                "pressure": 1008,
                "humidity": 74,
                "sea_level": 1008,
                "grnd_level": 1007
            },
            "visibility": 4000,
            "wind": {
                "speed": 5.14,
                "deg": 330
            },
            "clouds": {
                "all": 75
            },
            "dt": 1762067519,
            "sys": {
                "type": 1,
                "id": 9114,
                "country": "IN",
                "sunrise": 1762042283,
                "sunset": 1762082926
            },
            "timezone": 19800,
            "id": 1277155,
            "name": "Bara Bazar",
            "cod": 200
            }
                    
            return data
        
    except Exception as e:
        raise HTTPException(e)
        
        
    