from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = "postgresql://default:s4hSYAHaZ3qV@ep-royal-field-12424934.us-east-1.postgres.vercel-storage.com:5432/verceldb"

# SQLALCHEMY_DATABASE_URL = "postgresql://ntue:ntuedtd@db:5432/ntue"

# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL)

SQLALCHEMY_DATABASE_URL = "sqlite:///./ami.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()