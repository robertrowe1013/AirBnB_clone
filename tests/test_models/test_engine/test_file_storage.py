#!/usr/bin/python3
"""unittest for filestorage"""
import unittest
import os
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class TestFileStorage(unittest.TestCase):
    """class to test FileSTorage"""
    def test_class_variables(self):
        """class var test"""
        fs1 = FileStorage()
        list_app = []
        if os.path.exists('file.json'):
            os.remove('file.json')
        for exists in fs1.all().keys():
            list_app.append(fs1.all()[exists])
        for exists in list_app:
            del fs1.all()[exists.__class__.__name__ + '.' + exists.id]

        self.assertFalse(hasattr(FileStorage, '__file_path'))
        self.assertFalse(hasattr(FileStorage, '__objects'))
        self.assertFalse(hasattr(fs1, '__file_path'))
        self.assertFalse(hasattr(fs1, '__objects'))
        del fs1
        if os.path.exists('file.json'):
            print('file still exists')
            os.remove('file.json')
