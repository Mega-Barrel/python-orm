from typing import Optional
from sqlmodel import (
    Field, 
    Session, 
    SQLModel, 
    create_engine,
    select,
    or_,
    col
)

class Hero(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    secret_name: str
    age: Optional[int] = Field(default=None, index=True)

# Create engine
sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

# create engine
engine = create_engine(sqlite_url, echo=True)

def create_db_and_tables():
    # creating table
    SQLModel.metadata.create_all(engine)
    
def create_heros():
    hero_1 = Hero(name="Deadpond", secret_name="Dive Wilson")
    hero_2 = Hero(name="Spider-Boy", secret_name="Pedro Parqueador")
    hero_3 = Hero(name="Rusty-Man", secret_name="Tommy Sharp", age=48)
    hero_4 = Hero(name="Tarantula", secret_name="Natalia Roman-on", age=32)
    hero_5 = Hero(name="Black Lion", secret_name="Trevor Challa", age=35)
    hero_6 = Hero(name="Dr. Weird", secret_name="Steve Weird", age=36)
    hero_7 = Hero(name="Captain North America", secret_name="Esteban Rogelios", age=93)

    
    with Session(engine) as session:    
        session.add(hero_1)
        session.add(hero_2)
        session.add(hero_3)
        session.add(hero_4)
        session.add(hero_5)
        session.add(hero_6)
        session.add(hero_7)
        # Commit the changes
        session.commit()
        
def select_heroes():
    with Session(engine) as session:
        # statement = select(Hero).where(or_(col(Hero.age) <= 35, col(Hero.age) > 90))
        # hero = session.exec(select(Hero).where(Hero.name == 'Deadpond')).one()
        statement = select(Hero).offset(6).limit(3)
        results = session.exec(statement)
        heros = results.all()
        print(f"Heros: {heros}")
        # for result in results:
        #     print(result)
    
def main():
    create_db_and_tables()
    # create_heros()
    select_heroes()
        
if __name__ == "__main__":    
    main()