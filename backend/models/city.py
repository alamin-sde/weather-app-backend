from datetime import datetime, timezone
from typing import List
from sqlalchemy import Float, ForeignKey, String, Text, Boolean, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from core.database import Base
class City(Base):
    __tablename__ = "cities"
    id:Mapped[int]=mapped_column(primary_key=True)
    name:Mapped[str]=mapped_column(String(100))
    countryName:Mapped[str]=mapped_column(String(100))
    latitude:Mapped[float]=mapped_column(Float)
    longitude:Mapped[float]=mapped_column(Float)
    isActive: Mapped[bool] = mapped_column(Boolean, default=True)
    createdAt: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=lambda: datetime.now(timezone.utc)
    )
    updatedAt: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
    )
    userId:Mapped[int]=mapped_column(ForeignKey("users.id"))

    