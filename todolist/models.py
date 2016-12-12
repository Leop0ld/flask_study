from sqlalchemy import Column, Integer, String, Boolean
from database import Base


class Todo(Base):
    __tablename__ = 'todos'
    id = Column(Integer, primary_key=True)
    title = Column(String(128), unique=False)
    is_complete = Column(Boolean(), default=0)

    def __init__(self, name=None):
        self.name = name

    def __repr__(self):
        return '<Todo %d>' % self.id
