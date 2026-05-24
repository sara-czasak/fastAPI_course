from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


# URL to create location of database for application
SQLALCHEMY_DATABASE_URL = 'sqlite:///./todosapp.db'

# Create db engine (allow only one thread to connect to db to prevent accidental sharing of the same connection)
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False})

# Create a session local
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create an object of the db to be able to control db later
Base = declarative_base()

