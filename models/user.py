#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = "users"

    email = Column(String(128), nullabe = False)
    password = Column(String(128), nullabe = False)
    first_name = Column(String(128), nullabe = False)
    last_name = Column(String(128), nullabe = False)
