from typing import (
    Optional,
    List
)

from sqlmodel import (
    Field, 
    Session, 
    SQLModel, 
    create_engine,
    select,
    or_,
    col,
    Relationship
)

class Team(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    headquarters: str
    
    heroes: List['Hero'] = Relationship(back_populates="team")

class Hero(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    secret_name: str
    age: Optional[int] = Field(default=None, index=True)
    
    # foreign_key
    team_id: Optional[int] = Field(default=None, foreign_key='team.id')
    team: Optional[Team] = Relationship(back_populates='heroes')

# Create engine
sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

# create engine
engine = create_engine(sqlite_url, echo=True)

def create_db_and_tables():
    # creating table
    SQLModel.metadata.create_all(engine)

def add_heros():
    with Session(engine) as session:
        # Adding Team data
        team_preventers = Team(name="Preventers", headquarters="Sharp Tower")
        team_z_force = Team(name="Z-force", headquarters="Sister Margaret's Bar")
        
        # Adding Hero data
        hero_deadpond = Hero(name="Deadpond", secret_name="Dive Wilson", team=team_z_force)
        hero_rusty_man = Hero(name="Rusty-Man", secret_name="Tommy Sharp", age=48, team=team_preventers)
        hero_spider_boy = Hero(name="Spider-Boy", secret_name="Pedro Parqueador")
        
        session.add(hero_deadpond)
        session.add(hero_rusty_man)
        session.add(hero_spider_boy)
        session.commit()
        
        session.refresh(hero_deadpond)
        session.refresh(hero_rusty_man)
        session.refresh(hero_spider_boy)

        print("Created hero:", hero_deadpond)
        print("Created hero:", hero_rusty_man)
        print("Created hero:", hero_spider_boy)
        
        hero_spider_boy.team = team_preventers
        session.add(hero_spider_boy)
        session.commit()
        session.refresh(hero_spider_boy)
        print(f"Updated hero: {hero_spider_boy}")
        
        hero_black_lion = Hero(name="Black lion", secret_name="Trevor Challa", age=35)
        hero_sure_e = Hero(name="Princess Sure-E", secret_name="Sure-E")
        
        team_wakaland = Team(name="Wakaland", headquarters="Wakaland Capital City", heroes=[hero_black_lion, hero_sure_e])
        session.add(team_wakaland)
        session.commit()
        session.refresh(team_wakaland)
        print(f"Team Wakaland: {team_wakaland}")
        
        hero_tarantula = Hero(name="Tarantula", secret_name="Natalia Roman-on", age=32)
        hero_dr_weird = Hero(name="Dr. Weird", secret_name="Steve Weird", age=36)
        hero_cap = Hero(name="Captain North America", secret_name="Esteban Rogelios", age=93)
        
        team_preventers.heroes.append(hero_tarantula)
        team_preventers.heroes.append(hero_dr_weird)
        team_preventers.heroes.append(hero_cap)
        session.add(team_preventers)
        session.commit()
        session.refresh(hero_tarantula)
        session.refresh(hero_dr_weird)
        session.refresh(hero_cap)
        
        print("Preventers new hero:", hero_tarantula)
        print("Preventers new hero:", hero_dr_weird)
        print("Preventers new hero:", hero_cap)
        
        
def select_heros():
    with Session(engine) as session:
        # statement = select(Hero, Team).where(Team.id == Hero.team_id)
        statement = select(Team).where(Team.name == "Preventers")
        result = session.exec(statement=statement)
        team_preventers = result.one()
        
        print(f"Preventers: {team_preventers.heroes}")

def main():
    create_db_and_tables()
    # add_heros()
    select_heros()

if __name__ == "__main__":    
    main()