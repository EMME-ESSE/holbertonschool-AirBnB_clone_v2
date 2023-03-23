#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column
from sqlalchemy.orm import relationship

class State(BaseModel, Base):
    """ State class """

    name = ""
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    from os import environ
    
    if environ.get("HBNB_TYPE_STORAGE") == "db":
        cities = relationship("City", backref="state", cascade="delete")
    if environ.get("HBNB_TYPE_STORAGE") == "file":
        @property
        def cities(self):
            """ getter attr """
            from models import storage
            from models.city import City
            new_list = []
            for instance in storage.all():
                if isinstance(instance, City):
                    if instance.state_id == self.id:
                        new_list.append(instance)
            return new_list
                
