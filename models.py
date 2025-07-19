from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Date, Integer, String, Boolean

class Base(DeclarativeBase):
    """SQLAlchemy 2.0-style declarative base."""
    pass

class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    deadline = Column(Date, nullable=True)
    completed = Column(Boolean, default=False)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "deadline": self.deadline.isoformat() if self.deadline is not None else None,
            "completed": self.completed
        }
