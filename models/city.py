#!/usr/bin/python3
""" City Module for HBNB project """
from sqlalchemy import Column, String, ForeignKey
from models.base_model import Base, BaseModel


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = "cities"
    name = Column('name', String(128), nullable=False)
    state_id = Column('state_id', ForeignKey('states.id'), String(60), nullable=False)
