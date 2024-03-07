import cmd
from models.base_model import BaseModel
from models.user import User
from models import storage

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    valid_classes = ["BaseModel"]  # Add more valid classes here

   


    def do_create(self, args):
        """Create a new instance of a BaseModel or User"""
        if not args:
            print("** class name missing **")
            return
        class_name = args.split()[0]
        if class_name not in ["BaseModel", "User"]:
            print("** class doesn't exist **")
            return
        if class_name == "BaseModel":
            obj = BaseModel()
        else:
            obj = User()
        print(obj.id)
        obj.save()

    def do_show(self, args):
        """Prints the string representation of an instance"""
        if not args:
            print("** class name missing **")
            return
        arg_list = args.split()
        if arg_list[0] not in ["BaseModel", "User"]:
            print("** class doesn't exist **")
            return
        if len(arg_list) == 1:
            print("** instance id missing **")
            return
        key = arg_list[0] + "." + arg_list[1]
        if key in storage.all():
            print(storage.all()[key])
        else:
            print("** no instance found **")

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id"""
        if not args:
            print("** class name missing **")
            return
        arg_list = args.split()
        if arg_list[0] not in ["BaseModel", "User"]:
            print("** class doesn't exist **")
            return
        if len(arg_list) == 1:
            print("** instance id missing **")
            return
        key = arg_list[0] + "." + arg_list[1]
        if key in storage.all():
            del storage.all()[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_update(self, args):
        """Updates an instance based on the class name and id"""
        if not args:
            print("** class name missing **")
            return
        arg_list = args.split()
        if arg_list[0] not in ["BaseModel", "User"]:
            print("** class doesn't exist **")
            return
        if len(arg_list) == 1:
            print("** instance id missing **")
            return
        key = arg_list[0] + "." + arg_list[1]
        if key not in storage.all():
            print("** no instance found **")
            return
        if len(arg_list) == 2:
            print("** attribute name missing **")
            return
        if len(arg_list) == 3:
            print("** value missing **")
            return
        obj = storage.all()[key]
        setattr(obj, arg_list[2], arg_list[3])
        obj.save()

    def do_all(self, args):
        """Prints all string representations of instances"""
        arg_list = args.split()
        obj_list = []
        if not arg_list:
            for obj in storage.all().values():
                obj_list.append(str(obj))
            print(obj_list)
            return
        if arg_list[0] not in ["BaseModel", "User"]:
            print("** class doesn't exist **")
            return
        for obj in storage.all().values():
            if type(obj).__name__ == arg_list[0]:
                obj_list.append(str(obj))
        print(obj_list)
        
    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()