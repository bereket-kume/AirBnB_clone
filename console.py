#!/usr/bin/python3
import cmd

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"
    def do_create(self):
        pass

    def do_show(self):
        pass

    def do_destroy(self):
        pass

    def do_all(self):
        pass
    def do_count(self):
        pass

    def do_update(self):
        pass
    
    def do_help(self, line):
        if line == 'quit':
            print('Quit command to exit the program\n')
        else:
            print("\nDocumented commands (type help <topic>):\
                    \n========================================\
                    \nEOF  help  quit\n")

    def do_quit(self, line):
        return True

    def do_EOF(self, line):
        return True
    
    def emptyline(self):
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
