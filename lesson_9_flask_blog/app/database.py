from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

engine = create_engine(
    "sqlite:///app.db",
    echo=True
)

Session = sessionmaker(bind=engine)


class Base(DeclarativeBase):
    pass


def create_db():
    """
    Ініціалізація метаданих,
    створує базу даних, якщо відсутня,
    створює таблиці на основі моделей(Що спадкуються від Base) якщо жодної немає
    """
    Base.metadata.create_all(engine)


def drop_db():
    """
    Деконструкція метаданих,
    видалає усі таблиці з бази даних
    """
    Base.metadata.drop_all(engine)
