#!/usr/bin/python3

from models.base_model import BaseModel


class Amenity(BaseModel):
    """create class called Amenity"""

    def __init__(self):
        super().__init__()
        self.name = ""
