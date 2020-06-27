#!/usr/bin/python3
"""command line interpreter"""
import cmd
import shlex

class HBNBCommand(cmd.Cmd):
    """CLI"""
    prompt = '(hbnb)'

    def do_quit(self, line):
        """quits"""
        raise SystemExit

    def do_EOF(self, line):
        """end of file"""
        print('')
        return True

    def do_create(self, line):
        """make a new basemodel"""
        if line == "BaseModel":
            print("Not yet implemented")
        elif line:
            print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, line):
        """show instance of class and id"""
        args = line.split(" ")
        if args[0] == "BaseModel":
            try:
                args[1]
            except IndexError:
                print("** instance id missing **")
                return
            if args[1] == "idnum":
                print("ID num not yet implemented")
            else:
                print("** no instance found **")
        elif args[0]:
            print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_destroy(self, line):
        """delete instance based on class and id"""
        args = line.splint(" ")
        if args[0] == "BaseModel":
            try:
                args[1]
            except IndexError:
                print("** instance id missing **")
                return
            if args[1] == "idnum":
                print("ID num not yet implemented")
            else:
                print("** no instance found **")
        elif args[0]:
            print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_all(self, line):
        """print all instances or all class instances"""
        if line == "BaseModel":
            print("Class all Not yet implemented")
        elif line:
            print("** class doesn't exist **")
        else:
            print("Print All Not yet implemented")

    def do_update(self, line):
        """add or update attribute"""
        args = shlex.split(line)
        try:
            args[0]
        except IndexError:
            print("** class name missing **")
            return
        if args[0] == "BaseModel":
            try:
                args[1]
            except IndexError:
                print("** instance id missing **")
                return
            if args[1] == "idnum":
                print("ID num not yet implemented")
                try:
                    args[2]
                except IndexError:
                    print("** attribute name missing **")
                    return
                try:
                    args[3]
                except IndexError:
                    print("** value missing **")
                    return
                print("Update not yet implemented")
            else:
                print("** no instance found **")
                return
        else:
            print("** class doesn't exist **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
