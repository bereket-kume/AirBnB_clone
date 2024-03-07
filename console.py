#!/usr/bin/python3
import cmd

class HBNBCommand(cmd.Cmd):
    def do_help(self, line):
        print("i'm working")
    def do_quit(self, line):
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
