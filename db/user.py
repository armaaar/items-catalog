from sqlalchemy import *
from _base import Base

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, index=True)

    @property
    def serialize(self):
       """Return object data in easily serializeable format"""
       return {
            'id'           : self.id,
            'name'         : self.name,
            'email'        : self.email,
       }
