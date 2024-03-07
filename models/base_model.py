import json
from datetime import datetime
import uuid
import models
class BaseModel:
    __objects = {}

    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            self.id = kwargs.get("id", str(uuid.uuid4()))
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def save(self):
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        new_dict = self.__dict__.copy()
        new_dict.update({"__class__": self.__class__.__name__})
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict

    @classmethod
    def all(cls):
        return cls.__objects

    @classmethod
    def new(cls, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        cls.__objects[key] = obj

    @classmethod
    def save(cls):
        file_path = cls.__name__ + ".json"
        obj_dict = {}
        for key, value in cls.__objects.items():
            obj_dict[key] = value.to_dict()
        with open(file_path, mode="w", encoding="utf-8") as file:
            json.dump(obj_dict, file)

    @classmethod
    def reload(cls):
        file_path = cls.__name__ + ".json"
        try:
            with open(file_path, mode="r", encoding="utf-8") as file:
                obj_dict = json.load(file)
                for key, value in obj_dict.items():
                    cls.__objects[key] = cls(**value)
        except FileNotFoundError:
            pass