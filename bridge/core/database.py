from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from datetime import datetime

Base = declarative_base()

class MissionDB(Base):
    __tablename__ = 'missions'
    id = Column(Integer, primary_key=True)
    objective = Column(String)
    status = Column(String)
    data = Column(JSON)
    created_at = Column(DateTime, default=datetime.now)

# Add more tables later: artifacts, memories, etc.

def get_db_url():
    return os.getenv("DATABASE_URL", "sqlite:///living_bridge.db")

engine = create_engine(get_db_url())
SessionLocal = sessionmaker(bind=engine)

def init_db():
    Base.metadata.create_all(bind=engine)
