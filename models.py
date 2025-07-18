from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, String, Boolean

class Base(DeclarativeBase):
    """SQLAlchemy 2.0-style declarative base."""
    pass

class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    completed = Column(Boolean, default=False)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "completed": self.completed
        }
