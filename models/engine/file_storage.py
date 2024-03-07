import json
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
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
        elif class_name == "Place":
            obj = Place(**obj_dict)
        elif class_name == "State":
            obj = State(**obj_dict)
        elif class_name == "City":
            obj = City(**obj_dict)
        elif class_name == "Amenity":
            obj = Amenity(**obj_dict)
        elif class_name == "Review":
            obj = Review(**obj_dict)
        else:
            obj = BaseModel(**obj_dict)
        return obj

    def _serialize(self, obj):
        obj_dict = obj.to_dict()
        if isinstance(obj, User):
            obj_dict["__class__"] = "User"
        elif isinstance(obj, Place):
            obj_dict["__class__"] = "Place"
        elif isinstance(obj, State):
            obj_dict["__class__"] = "State"
        elif isinstance(obj, City):
            obj_dict["__class__"] = "City"
        elif isinstance(obj, Amenity):
            obj_dict["__class__"] = "Amenity"
        elif isinstance(obj, Review):
            obj_dict["__class__"] = "Review"
        else:
            obj_dict["__class__"] = "BaseModel"
        return obj_dict

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        json_dict = {}
        for key, value in FileStorage.__objects.items():
            json_dict[key] = self._serialize(value)
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(json_dict, f, indent=4)

    def reload(self):
        try:
            with open(FileStorage.__file_path, 'r') as f:
                json_dict = json.load(f)
                for key, value in json_dict.items():
                    class_name, obj_id = key.split('.')
                    class_ = eval(class_name)
                    obj = self._deserialize(value)
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass