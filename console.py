#!/usr/bin/python3

import cmd
import sys


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program on EOF (Ctrl+D)"""
        print()  # Print a new line before exiting
        return True

    def emptyline(self):
        """Do nothing on empty line"""
        pass

    def postcmd(self, stop, line):
        """Called after a command completes"""
        if not sys.stdin.isatty():
            return True


if __name__ == '__main__':
    if not sys.stdin.isatty():
        data = sys.stdin.read()
        HBNBCommand().onecmd(data)
    else:
        HBNBCommand().cmdloop()
