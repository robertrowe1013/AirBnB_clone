#!/usr/bin/python3
"""test pep8"""
import unittest
import pep8


class TestCodeFormat(unittest.TestCase):
    """test pep8"""
    def test_pep8_base_model(self):
        """test pep8 base.py"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0)
