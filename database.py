from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

# 1. Create an Engine; pointing at a local SQLite file
engine = create_engine(
    "sqlite:///tasks.db",
    echo=False,
    future=True,          # opt-in to SQLAlchemy 2.0 style
)

# 2. Configure a session factory
SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
    expire_on_commit=False,
    future=True,
)

def init_db() -> None:
    """
    Create all tables (if they don't exist yet) based on models' metadata.
    """
    Base.metadata.create_all(bind=engine)
