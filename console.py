#!/usr/bin/python3
"""command line interpreter"""
import cmd
import shlex
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """CLI"""
    prompt = '(hbnb)'
    class_name = ['BaseModel', 'User', 'State', 'City', 'Amenity', 'Place', 'Review']
    def do_quit(self, line):
        """quits"""
        raise SystemExit

    def do_EOF(self, line):
        """end of file"""
        print('')
        return True

    def do_create(self, line):
        """make a new instance"""
        if line in self.class_name:
            class_dict = {'BaseModel':BaseModel(), 'User':User(), 'State':State(),
                          'City':City(), 'Amenity':Amenity(), 'Place':Place(), 
                          'Review':Review()}
            for key in class_dict.keys():
                if key == line:
                    new_obj = class_dict[key]
                    new_obj.save()
                    print(new_obj.id)
        elif line:
            print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, line):
        """show instance of class and id"""
        args = line.split(" ")
        if args[0] in self.class_name:
            try:
                args[1]
            except IndexError:
                print("** instance id missing **")
                return
            show_key = args[0] + '.' + args[1]
            all_obj = storage.all()
            if show_key in all_obj:
                print(all_obj[show_key])
            else:
                print("** no instance found **")
        elif args[0]:
            print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_destroy(self, line):
        """delete instance based on class and id"""
        args = line.split(" ")
        if args[0] in self.class_name:
            try:
                args[1]
            except IndexError:
                print("** instance id missing **")
                return
            dest_key = args[0] + '.' + args[1]
            all_obj = storage.all()
            if dest_key in all_obj:
                del all_obj[dest_key]
            else:
                print("** no instance found **")
        elif args[0]:
            print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_all(self, line):
        """print all instances or all class instances"""
        if line in self.class_name:
            all_obj = storage.all()
            all_int = []
            for keys in all_obj.keys():
                if line == all_obj[keys].__class__.__name__:
                    all_int.append(str(all_obj[keys]))
            print(all_int)
        elif line:
            print("** class doesn't exist **")
        else:
            print("Print all objects")

    def do_update(self, line):
        """add or update attribute"""
        args = shlex.split(line)
        try:
            args[0]
        except IndexError:
            print("** class name missing **")
            return
        if args[0] in self.class_name:
            try:
                args[1]
            except IndexError:
                print("** instance id missing **")
                return
            update_key = args[0] + '.' + args[1]
            all_obj = storage.all()
            if update_key in all_obj:
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
        else:
            print("** class doesn't exist **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
