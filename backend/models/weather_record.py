from datetime import datetime, timezone
from typing import List
from core.database import Base
from sqlalchemy import Float,String,DateTime,Boolean,ForeignKey
from sqlalchemy.orm import Mapped,mapped_column,relationship
class WeatherRecord(Base):
    __tablename__="weather_records"
    id:Mapped[int]=mapped_column(primary_key=True)
    temperature:Mapped[float]=mapped_column(Float)
    humidity:Mapped[float]=mapped_column(Float)
    pressure:Mapped[float]=mapped_column(Float)
    wind_speed:Mapped[float]=mapped_column(Float)
    condition:Mapped[str]=mapped_column(String(100))
    aqi:Mapped[float]=mapped_column(Float)
    isActive: Mapped[bool] = mapped_column(Boolean, default=True)
    createdAt: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=lambda: datetime.now(timezone.utc)
    )
    updatedAt: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
    )
    city_id:Mapped[int]=mapped_column(ForeignKey("cities.id"))
    city=relationship("City",back_populates="weather_records")
    