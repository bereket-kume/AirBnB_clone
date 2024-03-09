#!/usr/bin/python3

from models.base_model import BaseModel


class User(BaseModel):
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    @classmethod
    def count(cls):
        """Count the number of User instances"""
        # Access the storage or database to retrieve the count of User instances
        # Implement your logic here to count the instances
        # Return the count
        return len(cls.all())
