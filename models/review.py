#!/usr/bin/python3

from models.base_model import BaseModel

class Review(BaseModel):
    """create class called review"""

    def __init__(self):
        super().__init__()
        self.place_id = ""
        self.user_id = ""
        self.text = ""