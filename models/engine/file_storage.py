import json
from models.user import User

from models.base_model import BaseModel
class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def _deserialize(self, obj_dict):
        class_name = obj_dict.get("__class__")
        if class_name == "User":
            obj = User(**obj_dict)
        else:
            obj = BaseModel(**obj_dict)
        return obj

    def _serialize(self, obj):
        obj_dict = obj.to_dict()
        if isinstance(obj, User):
            obj_dict["__class__"] = "User"
        else:
            obj_dict["__class__"] = "BaseModel"
        return obj_dict
    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        json_dict = {}
        for key, value in FileStorage.__objects.items():
            json_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(json_dict, f, indent=4)

    def reload(self):
        try:
            with open(FileStorage.__file_path, 'r') as f:
                json_dict = json.load(f)
                for key, value in json_dict.items():
                    class_name, obj_id = key.split('.')
                    module_name = class_name.lower()
                    class_ = eval(class_name)
                    obj = class_(**value)
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass