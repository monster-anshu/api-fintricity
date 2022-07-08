from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

POSTGRES_URI = 'postgresql://postgres:Niks1999@18.157.52.46:5432/postgres'

engin = create_engine( POSTGRES_URI)

SessionLocal = sessionmaker( autocommit=False,autoflush=False,bind=engin )

def getDB():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()