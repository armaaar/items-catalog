from sqlalchemy import *
from _base import Base

class Category(Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    @property
    def serialize(self):
       """Return object data in easily serializeable format"""
       return {
            'id'           : self.id,
            'name'         : self.name,
       }
