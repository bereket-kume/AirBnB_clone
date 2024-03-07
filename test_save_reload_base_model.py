import json
from models.base_model import BaseModel

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        json_dict = {}
        for key, value in FileStorage.__objects.items():
            json_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(json_dict, f)

    def reload(self):
        try:
            with open(FileStorage.__file_path, 'r') as f:
                json_dict = json.load(f)
                for key, value in json_dict.items():
                    class_name, obj_id = key.split('.')
                    obj = BaseModel(**value)
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass