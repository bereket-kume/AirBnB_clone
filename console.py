import cmd
import sys
import models


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    classes = ["BaseModel"]

    def do_quit(self, arg):
        """Quit command to exit the program"""
        sys.exit(0)

    def do_EOF(self, arg):
        """Exit the program on EOF (Ctrl+D)"""
        print()  # Print a new line before exiting
        sys.exit(0)

    def emptyline(self):
        """Do nothing on empty line"""
        pass

    def do_create(self, arg):
        """Create a new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
            return
        if arg not in self.classes:
            print("** class doesn't exist **")
            return
        instance = models.classes[arg]()
        instance.save()
        print(instance.id)

    def do_show(self, arg):
        """Print the string representation of an instance"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = args[0] + "." + args[1]
        objects = models.storage.all()
        if key in objects:
            print(objects[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Delete an instance based on the class name and id"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = args[0] + "." + args[1]
        objects = models.storage.all()
        if key in objects:
            del objects[key]
            models.storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Print all string representations of instances"""
        objects = models.storage.all()
        if not arg:
            print([str(obj) for obj in objects.values()])
        elif arg not in self.classes:
            print("** class doesn't exist **")
        else:
            print([str(obj)
                  for key, obj in objects.items() if key.split(".")[0] == arg])

    def do_update(self, arg):
        """Update an instance based on the class name and id"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = args[0] + "." + args[1]
        objects = models.storage.all()
        if key not in objects:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        instance = objects[key]
        attribute = args[2]
        value = args[3]
        setattr(instance, attribute, value)
        instance.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
