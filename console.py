import cmd
import models

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    
    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program when EOF (Ctrl+D) is encountered"""
        print()
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it (to the JSON file), and prints the id"""
        if not arg:
            print("** class name missing **")
            return

        class_name = arg
        if class_name not in models.storage.all_classes():
            print("** class doesn't exist **")
            return

        new_instance = models.storage.create(class_name)
        models.storage.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in models.storage.all_classes():
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        instance = models.storage.get(class_name, instance_id)
        if instance:
            print(instance)
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id (save the change into the JSON file)"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in models.storage.all_classes():
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        instance = models.storage.get(class_name, instance_id)
        if instance:
            models.storage.delete(instance)
            models.storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representations of all instances based on the class name"""
        args = arg.split()

        if args and args[0] not in models.classes:
            print("** class doesn't exist **")
            return

        instances = []
        if args:
            class_name = args[0]
            for key, value in models.storage.all().items():
                if class_name in key:
                    instances.append(str(value))
        else:
            for value in models.storage.all().values():
                instances.append(str(value))

        print(instances)

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or updating an attribute"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in models.storage.all_classes():
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        instance = models.storage.get(class_name, instance_id)
        if not instance:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        if len(args) < 4:
            print("** value missing **")
            return

        attribute_name = args[2]
        attribute_value = args[3]

        setattr(instance, attribute_name, attribute_value)
        models.storage.save()
if __name__ == '__main__':
    HBNBCommand().cmdloop()