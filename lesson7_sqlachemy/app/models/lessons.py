from __future__ import annotations

from typing import Optional, List

from sqlalchemy import String, Table, Column, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base
from app.models.group import Group

lesson_group_assoc_table = Table(
    "lesson_group_assoc_table",
    Base.metadata,
    Column(
        "group_id",
        ForeignKey("groups.id"),
        primary_key=True
    ),
    Column(
        "lessons_id",
        ForeignKey("lesson.id"),
        primary_key=True
    )
)


class Lesson(Base):
    __tablename__ = "lesson"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(150))
    groups: Mapped[List[Group]] = relationship(secondary=lesson_group_assoc_table)

    def __repr__(self):
        return f"Lesson: {self.title}"