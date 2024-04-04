#!/usr/bin/python3
"""Amenity Module for HBNB project"""
from models.base_model import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel):
    """The Amenity class, contains information about amenities"""
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary="place_amenity", viewonly=False)

