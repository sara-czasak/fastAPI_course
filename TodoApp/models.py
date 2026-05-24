from database import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey


class Users(Base):
    # Table name
    __tablename__ = "users"

    # Columns
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True)
    username = Column(String, unique=True)
    first_name = Column(String)
    last_name = Column(String)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    role = Column(String)


class Todos(Base):
    # Table name
    __tablename__ = 'todos'

    # Columns
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    priority = Column(Integer)
    complete = Column(Boolean, default=False)
    # Key referencing a different table
    owner_id = Column(Integer, ForeignKey('users.id'))


