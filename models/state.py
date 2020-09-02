#!/usr/bin/python3
""" State Module for HBNB project."""
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import os
import models
from models.city import City


class State(BaseModel, Base):
    """ State class """

    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City",  backref="state", cascade="all,delete")
    if os.getenv("HBNB_TYPE_STORAGE") != 'db':
        @property
        def cities(self):
            """Get a list of all related City objects."""
            liste = []
            for city in list(models.storage.all(City).values()):
                if city.state_id == self.id:
                    liste.append(city)
            return liste
