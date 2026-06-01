import sqlite3
from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

Base = declarative_base()

class MissionModel(Base):
    __tablename__ = 'missions'
    id = Column(Integer, primary_key=True)
    objective = Column(String)
    constraints = Column(Text)
    status = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

class ArtifactModel(Base):
    __tablename__ = 'artifacts'
    id = Column(Integer, primary_key=True)
    artifact_id = Column(String, unique=True)
    type = Column(String)
    title = Column(String)
    content = Column(Text)
    timestamp = Column(DateTime, default=datetime.utcnow)

# Add more tables for memories, debates, etc.

def init_db(db_url='sqlite:///living_bridge.db'):
    engine = create_engine(db_url)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session()

print('Database initialized.')  # placeholder
