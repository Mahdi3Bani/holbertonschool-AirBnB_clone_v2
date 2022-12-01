#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel


class Amenity(BaseModel):
    if models.storage_t == 'db':
        from models.place import place_amenity
        __tablename__ = "amenities"
        name = Column(String(128), nullable=False)
    else:
        name = ""
