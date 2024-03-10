import json
from os.path import exists


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        serialized_objects = {}
        for key, obj in self.__objects.items():
            serialized_objects[key] = obj.to_dict()

        with open(self.__file_path, mode='w', encoding='utf-8') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        if exists(self.__file_path):
            with open(self.__file_path, mode='r', encoding='utf-8') as file:
                serialized_objects = json.load(file)

            from models.base_model import BaseModel
            for key, obj_dict in serialized_objects.items():
                class_name, obj_id = key.split('.')
                obj = BaseModel(**obj_dict)
                self.__objects[key] = obj
