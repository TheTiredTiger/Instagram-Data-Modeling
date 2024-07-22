import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    user_id = Column(Integer, primary_key=True)
    user_name = Column(String(250), nullable=False)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)

class Follower(Base):
    __tablename__ = 'follower'
    user_from_id = Column(Integer, ForeignKey('user_id'), nullable=False)
    user_to_id = Column(Integer, ForeignKey('user_id'), nullable=False)

class Comment(Base):
    __tablename__ = 'comment'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    comment_id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    comment_text = Column(String(500), nullable=False)
    author_id = Column(Integer, ForeignKey('user_id'))
    post_id = Column(Integer, ForeignKey('post_id'))
    """ person = relationship(User) """

    def to_dict(self):
        return {}
    
class Post(Base):
    post_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user_id'))

class Media(Base):
    media_id = Column(Integer, primary_key=True)
    media_type = Column(String(250))
    url = Column(String, nullable=False)
    post_id = Column(Integer, ForeignKey('post_id'))

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
