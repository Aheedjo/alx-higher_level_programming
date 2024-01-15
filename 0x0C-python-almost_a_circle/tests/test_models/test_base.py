#!/usr/bin/env python3
"""Unit test for the base class"""

import unittest
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle


class TestBaseClass(unittest.TestCase):
    """Test the Base class"""
    def setUp(self):
        Base._Base__nb_objects = 0

    def test_nb_objects_attr(self):
        """Test the private class attribute __nb_objects"""
        self.assertIsNotNone(Base._Base__nb_objects)
        self.assertEqual(Base._Base__nb_objects, 0)
        Base()
        Base()
        Base()
        self.assertEqual(Base._Base__nb_objects, 3)
    
    def test_default_id(self):
        """Test the instantiation of a base object with no given id"""
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_id(self):
        """Test when id is provided"""
        b1 = Base()
        b2 = Base(99)
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 99)
        self.assertEqual(b3.id, 2)

    def test_init_with_zero_id(self):
        b1 = Base(0)
        self.assertEqual(b1.id, 0)

    def test_init_with_negative_id(self):
        b1 = Base(-5)
        self.assertEqual(b1.id, -5)

    def test_init_with_large_id(self):
        b1 = Base(10**6)
        self.assertEqual(b1.id, 10**6)

    def test_kwargs(self):
        b1 = Base(id=99)
        self.assertEqual(b1.id, 99)
    
    def test_none(self):
        b1 = Base(None)
        self.assertEqual(b1.id, 1)
    
    def mod_id(self):
        b1 = Base(2)
        b1.id = 99
        self.assertEqual(b1.id, 99)
    
    def test_nb_instances_private(self):
        with self.assertRaises(AttributeError):
            print(Base(12).__nb_instances)
    
class TestBase_to_json_string(unittest.TestCase):
    """Unittests for testing to_json_string method of Base class."""

    def test_to_json_string_rectangle_type(self):
        r = Rectangle(10, 7, 2, 8, 6)
        self.assertEqual(str, type(Base.to_json_string([r.to_dictionary()])))

    def test_to_json_string_rectangle_one_dict(self):
        r = Rectangle(10, 7, 2, 8, 6)
        self.assertTrue(len(Base.to_json_string([r.to_dictionary()])) == 53)

    def test_to_json_string_rectangle_two_dicts(self):
        r1 = Rectangle(2, 3, 5, 19, 2)
        r2 = Rectangle(4, 2, 4, 1, 12)
        list_dicts = [r1.to_dictionary(), r2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 106)

    def test_to_json_string_square_type(self):
        s = Square(10, 2, 3, 4)
        self.assertEqual(str, type(Base.to_json_string([s.to_dictionary()])))

    def test_to_json_string_square_one_dict(self):
        s = Square(10, 2, 3, 4)
        self.assertTrue(len(Base.to_json_string([s.to_dictionary()])) == 39)

    def test_to_json_string_square_two_dicts(self):
        s1 = Square(10, 2, 3, 4)
        s2 = Square(4, 5, 21, 2)
        list_dicts = [s1.to_dictionary(), s2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 78)

    def test_to_json_string_empty_list(self):
        self.assertEqual("[]", Base.to_json_string([]))

    def test_to_json_string_none(self):
        self.assertEqual("[]", Base.to_json_string(None))

    def test_to_json_string_no_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_to_json_string_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.to_json_string([], 1)


if __name__ == "__main__":
    unittest.main()

