from datetime import datetime, timezone
from typing import List
from sqlalchemy import Float, ForeignKey, String, Text, Boolean, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from core.database import Base
class QueryLog(Base):
    __tablename__='query_logs'
    id:Mapped[int]=mapped_column(primary_key=True)
    query_text:Mapped[str]=mapped_column(Text,nullable=False)
    extracted_city:Mapped[str]=mapped_column(String(100))
    ai_response:Mapped[str]=mapped_column(Text)
    isActive: Mapped[bool] = mapped_column(Boolean, default=True)
    createdAt: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=lambda: datetime.now(timezone.utc)
    )
    updatedAt: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
    )
    user_id:Mapped[int]=mapped_column(ForeignKey('users.id'))
    user=relationship("User",back_populates='query_logs')