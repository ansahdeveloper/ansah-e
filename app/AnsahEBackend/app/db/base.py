from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from app.core.config import settings
import random

# Create a connection pool for the primary database
primary_engine = create_engine(settings.SQLALCHEMY_DATABASE_URI, pool_size=20, max_overflow=0)

# Create connection pools for read replicas
replica_engines = [create_engine(f"postgresql://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@{server}/{settings.POSTGRES_DB}")
                   for server in settings.POSTGRES_REPLICA_SERVERS]

def get_db():
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=primary_engine)
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_read_db():
    if replica_engines:
        engine = random.choice(replica_engines)
    else:
        engine = primary_engine
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

