#!/usr/bin/python3

import cmd
import models
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print()
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass

    def do_create(self, arg):
        """Create a new instance of a class"""
        if not arg:
            print("** class name missing **")
            return

        class_name = arg.split()[0]
        classes = {"BaseModel": BaseModel, "User": User, "Place": Place, "State": State, "City": City, "Amenity": Amenity, "Review": Review}
        if class_name not in classes:
            print("** class doesn't exist **")
            return

        new_instance = classes[class_name]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Show the string representation of an instance"""
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        class_name = args[0]
        classes = {"BaseModel": BaseModel, "User": User, "Place": Place, "State": State, "City": City, "Amenity": Amenity, "Review": Review}
        if class_name not in classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        objects = storage.all()
        if key in objects:
            print(objects[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Delete an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        class_name = args[0]
        classes = {"BaseModel": BaseModel, "User": User, "Place": Place, "State": State, "City": City, "Amenity": Amenity, "Review": Review}
        if class_name not in classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        objects = storage.all()
        if key in objects:
            del objects[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Print string representation of all instances or of a specific class"""
        objects = storage.all()
        classes = {
                    "BaseModel": BaseModel,
                    "User": User, 
                    "Place": Place,
                    "State": State, 
                    "City": City, 
                    "Amenity": Amenity, 
                    "Review": Review}
        if not arg:
            print([str(obj) for obj in objects.values()])
            return

        class_name = arg.split()[0]
        if class_name not in classes:
            print("** class doesn't exist **")
            return

        instances = [str(obj) for key, obj in objects.items() if key.split('.')[0] == class_name]
        print(instances)

    def do_update(self, arg):
        """Update an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        class_name = args[0]
        classes = {
                "BaseModel": BaseModel,
                "User": User, 
                "Place": Place, 
                "State": State, 
                "City": City, 
                "Amenity": Amenity, 
                "Review": Review
                }
        if class_name not in classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        objects = storage.all()
        if key not in objects:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        if len(args) < 4:
            print("** value missing **")
            return
    def do_count(self, arg):

        classes = {
                "BaseModel": BaseModel,
                "User": User, 
                "Place": Place, 
                "State": State, 
                "City": City, 
                "Amenity": Amenity, 
                "Review": Review
                }

        if not arg:
            print("** class name missing **")
            return
        class_name = arg.split()[0]
        if class_name not in classes:
            print("** class doesn't exist **")
            return
        
            
if __name__ == '__main__':
    HBNBCommand().cmdloop()
