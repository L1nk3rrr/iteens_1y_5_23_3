from __future__ import annotations
from typing import Optional, List

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from flask_login import UserMixin

from app.database import Base


class User(Base, UserMixin):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    nickname: Mapped[Optional[str]] = mapped_column(String(50))
    email: Mapped[Optional[str]]
    password: Mapped[Optional[str]]
    events: Mapped[List["Event"]] = relationship(back_populates="user")

    def __repr__(self):
        return f"User {self.nickname}"

    def __str__(self):
        return self.nickname.capitalize()
