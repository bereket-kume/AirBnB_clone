#!/usr/bin/python3

from models.base_model import BaseModel
class State(BaseModel):
    """create class called state"""

    def __init__(self):
        super().__init__()
        self.name = ""