from __future__ import annotations

from typing import Optional, List

from sqlalchemy import String, Table, Column, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base
from .group import Group

student_group_assoc_table = Table(
    "student_group_assoc_table",
    Base.metadata,
    Column(
        "group_id",
        ForeignKey("groups.id"),
        primary_key=True
    ),
    Column(
        "student_id",
        ForeignKey("student.id"),
        primary_key=True
    )
)


class Student(Base):
    __tablename__ = "student"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    surname: Mapped[Optional[str]]
    age: Mapped[int]
    address: Mapped[str] = mapped_column(String(255))
    groups: Mapped[List[Group]] = relationship(secondary=student_group_assoc_table)

    def __repr__(self):
        return f"{self.name.title()} {self.surname.title()} Age: {self.age}"