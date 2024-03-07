import cmd
import json
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    classes = {"BaseModel": BaseModel}

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program using EOF"""
        print("\n")
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass

    def do_create(self, arg):
        """Create a new instance of BaseModel"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        instance = self.classes[class_name]()
        instance.save()
        print(instance.id)

    def do_show(self, arg):
        """Print the string representation of an instance"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        instances = BaseModel.all()
        if key not in instances:
            print("** no instance found **")
            return
        print(instances[key])

    def do_destroy(self, arg):
        """Delete an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        instances = BaseModel.all()
        if key not in instances:
            print("** no instance found **")
            return
        del instances[key]
        BaseModel.save()

    def do_all(self, arg):
        """Print all string representations of instances"""
        args = arg.split()
        instances = BaseModel.all()
        if not args:
            print([str(instance) for instance in instances.values()])
        else:
            class_name = args[0]
            if class_name not in self.classes:
                print("** class doesn't exist **")
                return
            print([str(instance) for instance in instances.values()
                   if instance.__class__.__name__ == class_name])

    def do_update(self, arg):
        """Update an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        instances = BaseModel.all()
        if key not in instances:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        attribute_name = args[2]
        if len(args) < 4:
            print("** value missing **")
            return
        attribute_value = args[3]
        instance = instances[key]
        setattr(instance, attribute_name, attribute_value)
        instance.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()