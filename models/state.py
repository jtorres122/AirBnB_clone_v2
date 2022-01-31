#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from AirBnB_clone_v2.models.city import City
from models.base_model import Base, BaseModel


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column('name', String(128), nullable=False)

    cities = relationship("City", backref="state")

    @property
    def cities(self):
        return repr(City)
