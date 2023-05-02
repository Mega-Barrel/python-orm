from typing import Optional
from sqlmodel import Field, Session, SQLModel, create_engine

class Hero(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: Optional[int] = None
    
hero_1 = Hero(id=1, name="Deadpond", secret_name="Dive Wilson")
hero_2 = Hero(id=2, name="Spider-Boy", secret_name="Pedro Parqueador")
hero_3 = Hero(id=3, name="Rusty-Man", secret_name="Tommy Sharp", age=48)

# Create engine
engine = create_engine("sqlite:///database.db")

# create table
SQLModel.metadata.create_all(engine)

with Session(engine) as session:
    session.add(hero1)
    session.add(hero2)
    session.add(hero3)