#!/bin/usr/python3
""" temp text """
from datetime import datetime
import uuid


class BaseModel():
    """ temp """

    def __init__(self, *args, **kwargs):
        """initializes BaseModel"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs is not None:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    time = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, time)
                elif key != "__class__":
                    setattr(self, key, value)

    def __str__(self):
        classname = self.__class__.__name__
        return "[{}] ({}) {}".format(classname, self.id, self.__dict__)

    def save(self):
        """updates updated_at with current time"""
        self.updated_at = datetime.now()


    def to_dict(self):
        self.dictionary = dict(self.__dict__)
        self.dictionary['__class__'] = self.__class__.__name__
        self.dictionary['created_at'] = datetime.isoformat(self.created_at)
        self.dictionary['updated_at'] = datetime.isoformat(self.updated_at)
        return self.dictionary
