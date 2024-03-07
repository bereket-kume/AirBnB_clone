import json
from os.path import exists


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):

        return self.__objects
    
    def new(self, obj):

        key="{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):

        serializable_objetcs = {
            key: obj.to_dict for key, obj in self.__objects.items()
        }

        with open(self.__file_path, "w") as file:
            json.dump(serializable_objetcs, file)

    def reload(self):

        if exists(self.__file_path):
            with open(self.__file_path, "r") as file:
                serializable_objects = json.load(file)
                for key, obj_dict in serializable_objects.items():
                    class_name, obj_id = key.split(".")
                    obj = eval(class_name)(**obj_dict)
                    self.__objects[key] = obj
                    