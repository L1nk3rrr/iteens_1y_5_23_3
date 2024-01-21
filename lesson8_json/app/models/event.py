from __future__ import annotations
from typing import Optional

from sqlalchemy import Column, Date, Time, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class Event(Base):
    __tablename__ = "events"

    id: Mapped[int] = mapped_column(primary_key=True)
    date = Column("date", Date)
    time = Column("time", Time, nullable=True,)
    header: Mapped[str] = mapped_column(String(80))
    description: Mapped[Optional[str]] = mapped_column(String(240))
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    # ORM object to have a user
    user: Mapped["User"] = relationship(back_populates="events")

    def __repr__(self):
        return f"Event: {self.header}"

    def __str__(self):
        return self.header.capitalize()
