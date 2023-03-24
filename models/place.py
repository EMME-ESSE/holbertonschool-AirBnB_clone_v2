#!/usr/bin/python3
""" module defines the place class """

import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship


class Place(BaseModel, Base):
    """ Class defiinition for place """

    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship("Review", cascade="all, delete-orphan",
                               backref='place')
        amenities = relationship("Amenity", secondary=place_amenity,
                                 backref="places", viewonly=False)
    else:
        @property
        def reviews(self):
            """getter Review """
            from models.review import Review
            reviews = []
            all_reviews = models.storage.all(Review)
            for review in all_reviews.values():
                if review.place_id == self.id:
                    reviews.append(models.storage.all(Review)[review])
            return reviews
