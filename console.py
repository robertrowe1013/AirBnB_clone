#!/usr/bin/python3
"""command line interpreter"""
import cmd

class HBNBCommand(cmd.Cmd):
    """CLI"""
    prompt = '(hbnb)'

    def do_quit(self, args):
        """quits"""
        raise SystemExit

    def do_EOF(self, args):
        """end of file"""
        print('')
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
