#!/usr/bin/python3
""" holds class User"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import hashlib


class User(BaseModel, Base):
    """Representation of a user"""
    if models.storage_t == 'db':
        __tablename__ = 'users'
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship("Place", backref="user")
        reviews = relationship("Review", backref="user")
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""

    def __init__(self, *args, **kwargs):
        """Initializes user"""
        super().__init__(*args, **kwargs)

        if 'password' in kwargs:
            self.password = hashlib.md5
            (kwargs['password'].encode()).hexdigest()

    def to_dict(self):
        """Returns a dictionary representation of User,
            excluding 'password'.
        """
        user_dict = super().to_dict()
        if 'password' in user_dict and models.storage_t != 'db':
            del user_dict['password']
        return user_dict
