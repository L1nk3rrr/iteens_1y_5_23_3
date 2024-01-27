from __future__ import annotations
from datetime import date

from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class Post(Base):
    __tablename__ = "post"

    id: Mapped[int] = mapped_column(primary_key=True)
    created_date: Mapped[date] = mapped_column(default=date.today())
    title: Mapped[str] = mapped_column(String(256))
    content: Mapped[str] = mapped_column(Text())

    def __repr__(self):
        return f"Post: {self.title}"

    def __str__(self):
        return self.title.capitalize()

