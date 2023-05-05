from typing import Optional
from sqlmodel import Field, Session, SQLModel, create_engine, select

class Hero(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: Optional[int] = None

# Create engine
sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

# create engine
engine = create_engine(sqlite_url)

def create_db_and_tables():
    # creating table
    SQLModel.metadata.create_all(engine)        
        
if __name__ == "__main__":    
    create_db_and_tables()