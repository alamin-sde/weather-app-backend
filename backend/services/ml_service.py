from typing import Dict,Any,List
from fastapi import HTTPException
import os
from openai import AsyncOpenAI
from typing import List, Any
from fastapi import HTTPException
from datetime import datetime
OPENAI_API_URL=os.getenv('OPENAI_API_URL')
OPENAI_API_KEY=os.getenv('OPENAI_API_KEY')
OPENAI_API_MODEL=os.getenv('OPENAI_API_MODEL')
client = AsyncOpenAI(base_url=OPENAI_API_URL, api_key=OPENAI_API_KEY)
async def get_llm_summary(weather_data:  Dict[str, Any])-> str:
    try:
        prompt = (
            f"Write a short, 1-2 sentence friendly human summary of this weather JSON:\n"
            f"{weather_data}"
        )
        completion = await client.chat.completions.create(
            model=OPENAI_API_MODEL,
            messages=[
                {
                    "role": "system",
                    "content": "You are a friendly assistant that summarizes weather information for users.",
                },
                {
                    "role": "user",
                    "content": prompt,
                },
            ],
        )
        return completion.choices[0].message.content

    except Exception as e:
        raise HTTPException(e)
        

from typing import List, Any
from datetime import datetime
from fastapi import HTTPException

async def get_five_days_weather_summary(forecast_data: List[Any], target_date: datetime) -> str:
    try:
        prompt = f"""
You are given raw weather forecast data for {target_date.date()}.

### Forecast Data:
{forecast_data}

### Your Task:
- Calculate average temperature, humidity, and dominant condition.
- List hourly forecasts.
- Return a JSON in the specified format.
        """

        completion = await client.chat.completions.create(
            model=OPENAI_API_MODEL,
            messages=[
                {
                    "role": "system",
                    "content": "You are a friendly assistant that summarizes weather information for users.",
                },
                {
                    "role": "user",
                    "content": prompt.strip(),
                },
            ],
        )

        return completion.choices[0].message.content.strip()

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
