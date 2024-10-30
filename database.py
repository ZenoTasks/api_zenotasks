from sqlalchemy import create_engine
from sqlmodel import SQLModel, Session



DATABASE_URL = f"postgresql://postgres:postgres@db:5432/zenotasks"

engine = create_engine(DATABASE_URL,echo=True)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session