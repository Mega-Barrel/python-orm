from typing import Optional
from sqlmodel import (
    Field, 
    Session, 
    SQLModel, 
    create_engine, 
    select
)

class Hero(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: Optional[int] = None

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
    
    with Session(engine) as session:    
        session.add(hero_1)
        session.add(hero_2)
        session.add(hero_3)
        # Commit the changes
        session.commit()
        
def select_heroes():
    with Session(engine) as session:
        statement = session.exec(select(Hero)).all()
        print(statement)
        # for result in results:
        #     print(result)
        #     print()
    
def main():
    create_db_and_tables()
    # create_heros()
    select_heroes()
        
if __name__ == "__main__":    
    main()