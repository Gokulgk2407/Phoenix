
!pip install sqlalchemy

from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create in-memory SQLite database
engine = create_engine('sqlite:///:memory:', echo=True)
Base = declarative_base()

class Movie(Base):
  __tablename__ = 'movies'
  id = Column(Integer, primary_key=True)
  name = Column(String)
  year = Column(Integer)
  genre = Column(String)
  release_date = Column(Date)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
gokul
