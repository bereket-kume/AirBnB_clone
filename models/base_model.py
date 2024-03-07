#!/usr/bin/python3
import uuid
from datetime import datetime

class BaseModel:
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.item():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                        setattr(self, key, value)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
    
    def save(self):
        self.update_at = datetime.now()

    def to_dict(self):
        Dict = self.__dict__.copy()
        Dict['__class__'] = self.__class__.__name__
        Dict['created_at'] = self.created_at.isoformat()
        Dict['updated_at'] = self.updated_at.isoformat()
        return Dict
