from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from _base import Base

from category import Category
from user import User
from item import Item


engine = create_engine('sqlite:///test.db')
Base.metadata.create_all(engine, checkfirst=True)
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
db_session = DBSession()

__all__ = ["db_session", "Category", "User", "Item"]
