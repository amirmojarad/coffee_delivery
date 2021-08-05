from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# set db url and config, you can change it to postgress also
SQLALCHEMY_DATABASE_URL = "sqlite:///./db/sql_app.db"

# generate sql_alchemy engine, get the url to it and set connect args also
# set check same thread to False, it becomes in one thread also
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# make session for database with no autocommit and not autho flush and bind into engine that created before
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# create Base and we use this class for creating database models
Base = declarative_base()
