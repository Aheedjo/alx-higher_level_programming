#!/usr/bin/python3
"""This module contains tests for the rectangle class"""

import unittest
import io
import sys
from models.rectangle import Rectangle
from models.base import Base


class TestRectangleClass(unittest.TestCase):
    """Test Rectangle Class"""
    
    def setUp(self):
        Base._Base__nb_objects = 0

    def test_isinstance(self):
        self.assertIsInstance(Rectangle(98, 99), Base)

    def test_inheritance(self):
        """Tests if Rectangle inherits Base"""
        self.assertTrue(issubclass(Rectangle, Base))

    def test_empty_rect(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_no_height(self):
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_nb_objects_attr(self):
        """Test the private class attribute __nb_objects"""
        self.assertIsNotNone(Base._Base__nb_objects)
        self.assertEqual(Base._Base__nb_objects, 0)
        r1 = Rectangle(1, 2)
        Rectangle(11, 22)
        Rectangle(111, 222)
        self.assertEqual(Base._Base__nb_objects, 3)

    def test_empty_constructor(self):
        """Test empty constructor"""
        with self.assertRaises(TypeError) as e:
            r = Rectangle()

    def test_excess_constructor_args(self):
        """Tests constructor signature"""
        with self.assertRaises(TypeError) as e:
            r = Rectangle(1, 2, 3, 4, 5, 6)

    def test_intsance_id(self):
        """test default id"""
        r1 = Rectangle(10, 20)
        self.assertEqual(r1.id, 1)

        #test custom id
        r2 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r2.id, 5)

        #test three args
        r3 = Rectangle(10, 20, 1)
        self.assertEqual(r3.id, 2)

    def test_privacy(self):
        with self.assertRaises(AttributeError):
            width = Rectangle(10, 20, 1, 2, 99).__width

        with self.assertRaises(AttributeError):
            height = Rectangle(10, 20, 1, 2, 99).__height

        with self.assertRaises(AttributeError):
            x = Rectangle(10, 20, 1, 2, 9).__x

        with self.assertRaises(AttributeError):
            y = Rectangle(10, 20, 1, 2, 9).__y
    
    def test_getters(self):
        r1 = Rectangle(10, 20, 1, 2, 99)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 20)
        self.assertEqual(r1.x, 1)
        self.assertEqual(r1.y, 2)

    def test_setters(self):
        r1 = Rectangle(10, 20, 1, 2, 99)
        r1.width = 100
        self.assertEqual(r1.width, 100)
        r1.height = 200
        self.assertEqual(r1.height, 200)
        r1.x = 10
        self.assertEqual(r1.x, 10)
        r1.y = 20
        self.assertEqual(r1.y, 20)

    def test_kwargs_instance(self):
        r1 = Rectangle(width=10, height=20, x=3, y=4)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 20)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 4)

    def test_args_instance(self):
        r1 = Rectangle(10, 20, 3, 4)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 20)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 4)

class TestRectangleWidth(unittest.TestCase):
    """Testing and validating rectangle width"""
    
    def test_None_width(self):
        with self.assertRaises(TypeError) as e:
            Rectangle(None, 1)
        msg = "width must be an integer"
        self.assertEqual(str(e.exception), msg)
    
    def test_str_width(self):
        with self.assertRaises(TypeError) as e:
            Rectangle("string", 1)
        msg = "width must be an integer"
        self.assertEqual(str(e.exception), msg)

    def test_nan_width(self):
        with self.assertRaises(TypeError) as e:
            Rectangle(float('nan'), 1)
        msg = "width must be an integer"
        self.assertEqual(str(e.exception), msg)

    def test_inf_width(self):
        with self.assertRaises(TypeError) as e:
            Rectangle(float('inf'), 1)
        msg = "width must be an integer"
        self.assertEqual(str(e.exception), msg)

    def test_float_width(self):
        with self.assertRaises(TypeError) as e:
            Rectangle(2.9, 1)
        msg = "width must be an integer"
        self.assertEqual(str(e.exception), msg)

    def test_complex_width(self):
        with self.assertRaises(TypeError) as e:
            Rectangle(complex(8), 1)
        msg = "width must be an integer"
        self.assertEqual(str(e.exception), msg)

    def test_dict_width(self):
        with self.assertRaises(TypeError) as e:
            Rectangle({"a": 1, "b": 2}, 2)
        msg = "width must be an integer"
        self.assertEqual(str(e.exception), msg)

    def test_bool_width(self):
        with self.assertRaises(TypeError) as e:
            Rectangle(True, 1)
        msg = "width must be an integer"
        self.assertEqual(str(e.exception), msg)

    def test_list_width(self):
        with self.assertRaises(TypeError) as e:
            Rectangle([1, 2, 3], 2)
        msg = "width must be an integer"
        self.assertEqual(str(e.exception), msg)

    def test_negative_width(self):
        with self.assertRaises(ValueError) as e:
            Rectangle(-9, 1)
        msg = "width must be > 0"
        self.assertEqual(str(e.exception), msg)\

    def test_zero_width(self):
        with self.assertRaises(ValueError) as e:
            Rectangle(0, 1)
        msg = "width must be > 0"
        self.assertEqual(str(e.exception), msg)


class TestRectangleHeight(unittest.TestCase):
    """Testing and validating rectangle height"""

    def test_None_height(self):
        with self.assertRaises(TypeError) as e:
            Rectangle(1, None)
        msg = "height must be an integer"
        self.assertEqual(str(e.exception), msg)

    def test_str_height(self):
        with self.assertRaises(TypeError) as e:
            Rectangle(1, "string")
        msg = "height must be an integer"
        self.assertEqual(str(e.exception), msg)

    def test_nan_height(self):
        with self.assertRaises(TypeError) as e:
            Rectangle(1, float('nan'))
        msg = "height must be an integer"
        self.assertEqual(str(e.exception), msg)

    def test_inf_height(self):
        with self.assertRaises(TypeError) as e:
            Rectangle(1, float('inf'))
        msg = "height must be an integer"
        self.assertEqual(str(e.exception), msg)

    def test_float_height(self):
        with self.assertRaises(TypeError) as e:
            Rectangle(1, 2.9)
        msg = "height must be an integer"
        self.assertEqual(str(e.exception), msg)

    def test_complex_height(self):
        with self.assertRaises(TypeError) as e:
            Rectangle(1, complex(8))
        msg = "height must be an integer"
        self.assertEqual(str(e.exception), msg)

    def test_dict_height(self):
        with self.assertRaises(TypeError) as e:
            Rectangle(1, {"a": 1, "b": 2})
        msg = "height must be an integer"
        self.assertEqual(str(e.exception), msg)

    def test_bool_height(self):
        with self.assertRaises(TypeError) as e:
            Rectangle(1, True)
        msg = "height must be an integer"
        self.assertEqual(str(e.exception), msg)

    def test_list_height(self):
        with self.assertRaises(TypeError) as e:
            Rectangle(1, [1, 2, 3])
        msg = "height must be an integer"
        self.assertEqual(str(e.exception), msg)

    def test_negative_height(self):
        with self.assertRaises(ValueError) as e:
            Rectangle(1, -9)
        msg = "height must be > 0"
        self.assertEqual(str(e.exception), msg)\

    def test_zero_height(self):
        with self.assertRaises(ValueError) as e:
            Rectangle(1, 0)
        msg = "height must be > 0"
        self.assertEqual(str(e.exception), msg)

class TestRectangleX(unittest.TestCase):
    """Testing and validating rectangle x"""

    def test_None_x(self):
        with self.assertRaises(TypeError) as e:
            Rectangle(1, 2, None)
        msg = "x must be an integer"
        self.assertEqual(str(e.exception), msg)

    def test_str_x(self):
        with self.assertRaises(TypeError) as e:
            Rectangle(1, 2, "string")
        msg = "x must be an integer"
        self.assertEqual(str(e.exception), msg)

    def test_nan_x(self):
        with self.assertRaises(TypeError) as e:
            Rectangle(1, 2, float('nan'))
        msg = "x must be an integer"
        self.assertEqual(str(e.exception), msg)

    def test_inf_x(self):
        with self.assertRaises(TypeError) as e:
            Rectangle(1, 2, float('inf'))
        msg = "x must be an integer"
        self.assertEqual(str(e.exception), msg)

    def test_float_x(self):
        with self.assertRaises(TypeError) as e:
            Rectangle(1, 2, 2.9)
        msg = "x must be an integer"
        self.assertEqual(str(e.exception), msg)

    def test_complex_x(self):
        with self.assertRaises(TypeError) as e:
            Rectangle(1, 2, complex(8))
        msg = "x must be an integer"
        self.assertEqual(str(e.exception), msg)

    def test_dict_x(self):
        with self.assertRaises(TypeError) as e:
            Rectangle(1, 2, {"a": 1, "b": 2})
        msg = "x must be an integer"
        self.assertEqual(str(e.exception), msg)

    def test_bool_x(self):
        with self.assertRaises(TypeError) as e:
            Rectangle(1, 2, True)
        msg = "x must be an integer"
        self.assertEqual(str(e.exception), msg)

    def test_list_x(self):
        with self.assertRaises(TypeError) as e:
            Rectangle(1, 2, [1, 2, 3])
        msg = "x must be an integer"
        self.assertEqual(str(e.exception), msg)

    def test_negative_x(self):
        with self.assertRaises(ValueError) as e:
            Rectangle(1, 2, -9)
        msg = "x must be >= 0"
        self.assertEqual(str(e.exception), msg)

    def test_zero_x(self):
        r1 = Rectangle(1, 2, 0)
        self.assertEqual(r1.x, 0)

class TestRectangleY(unittest.TestCase):
    """Testing and validating rectangle's y"""

    def test_None_y(self):
        with self.assertRaises(TypeError) as e:
            Rectangle(1, 2, 3, None)
        msg = "y must be an integer"
        self.assertEqual(str(e.exception), msg)

    def test_str_y(self):
        with self.assertRaises(TypeError) as e:
            Rectangle(1, 2, 3, "string")
        msg = "y must be an integer"
        self.assertEqual(str(e.exception), msg)

    def test_nan_y(self):
        with self.assertRaises(TypeError) as e:
            Rectangle(1, 2, 3, float('nan'))
        msg = "y must be an integer"
        self.assertEqual(str(e.exception), msg)

    def test_inf_y(self):
        with self.assertRaises(TypeError) as e:
            Rectangle(1, 2, 3, float('inf'))
        msg = "y must be an integer"
        self.assertEqual(str(e.exception), msg)

    def test_float_y(self):
        with self.assertRaises(TypeError) as e:
            Rectangle(1, 2, 3, 2.9)
        msg = "y must be an integer"
        self.assertEqual(str(e.exception), msg)

    def test_complex_y(self):
        with self.assertRaises(TypeError) as e:
            Rectangle(1, 2, 3, complex(8))
        msg = "y must be an integer"
        self.assertEqual(str(e.exception), msg)

    def test_dict_y(self):
        with self.assertRaises(TypeError) as e:
            Rectangle(1, 2, 3, {"a": 1, "b": 2})
        msg = "y must be an integer"
        self.assertEqual(str(e.exception), msg)

    def test_bool_y(self):
        with self.assertRaises(TypeError) as e:
            Rectangle(1, 2, 3, True)
        msg = "y must be an integer"
        self.assertEqual(str(e.exception), msg)

    def test_list_y(self):
        with self.assertRaises(TypeError) as e:
            Rectangle(1, 2, 3, [1, 2, 3])
        msg = "y must be an integer"
        self.assertEqual(str(e.exception), msg)

    def test_negative_y(self):
        with self.assertRaises(ValueError) as e:
            Rectangle(1, 2, 3, -9)
        msg = "y must be >= 0"
        self.assertEqual(str(e.exception), msg)

    def test_zero_y(self):
        r1 = Rectangle(1, 2, 3, 0)
        self.assertEqual(r1.y, 0)

class TestRectangleAttrOrder(unittest.TestCase):
    """Testing the order of attr init"""

    def test_width_before_height(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("invalid width", "invalid height")

    def test_width_before_x(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("invalid width", 99, "invalid x")

    def test_width_before_y(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("invalid width", 98, 99, "invalid y")

    def test_height_before_x(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(99, "invalid height", "invalid x")

    def test_height_before_y(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(98, "invalid height", 99, "invalid y")

    def test_x_before_y(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(98, 99, "invalid x", "invalid y")

class TestRectangleArea(unittest.TestCase):
    """Test the area() method"""

    def test_standard_input(self):
        r1 = Rectangle(10, 20)
        self.assertEqual(r1.area(), 200)

    def test_singleton(self):
        r1 = Rectangle(1, 1)
        self.assertEqual(r1.area(), 1)

    def test_zero_area(self):
        with self.assertRaises(ValueError):
            r1 = Rectangle(0, 0)
            self.assertEqual(r1.area(), 0)

    def test_large_area(self):
        r = Rectangle(999999999999999, 999999999999999999, 0, 0, 1)
        self.assertEqual(999999999999998999000000000000001, r.area())

    def test_changed_attributes(self):
        r = Rectangle(9, 10, 3, 14, 31)
        r.width = 7
        r.height = 14
        self.assertEqual(98, r.area())

    def test_area_one_arg(self):
        r = Rectangle(2, 10, 1, 1, 1)
        with self.assertRaises(TypeError):
            r.area(1)

class TestRectangleDisplay(unittest.TestCase):
    """Test the display() method"""

    @staticmethod
    def stdout_buffer(rectangle):
        """
        Returns text printed to stdout.

        Args:
            rectangle (Rectangle): The Rectangle to print to stdout.
        Returns:
            The text printed to stdout
        """
        
        #create a buffer to store the output
        buffer = io.StringIO()

        #redirect stdout to the buffer
        sys.stdout = buffer
        
        rectangle.display()
        
        # Restore sys.stdout to its original state
        sys.stdout = sys.__stdout__

        return buffer

    def test_standard_display(self):
        r = Rectangle(2, 3)
        output = TestRectangleDisplay.stdout_buffer(r)
        self.assertEqual(output.getvalue(), "##\n##\n##\n")

    def test_standard_display_plus(self):
        r = Rectangle(2, 4)
        output = TestRectangleDisplay.stdout_buffer(r)
        self.assertEqual(output.getvalue(), "##\n##\n##\n##\n")

    def test_display_singleton(self):
        r = Rectangle(1,1)
        output = TestRectangleDisplay.stdout_buffer(r)
        self.assertEqual(output.getvalue(), "#\n")
        

class TestRectangle__str__(unittest.TestCase):
    """Test string repr of the class"""

    @staticmethod
    def stdout_buffer(rectangle):
        """
        Returns text printed to stdout.

        Args:
            rectangle (Rectangle): The Rectangle to print to stdout.
        Returns:
            The text printed to stdout
        """

        buffer = io.StringIO()
        sys.stdout = buffer

        print(rectangle)
        
        sys.stdout = sys.__stdout__

        return buffer

    def test_standard__str__(self):
        r = Rectangle(4, 6, 2, 1, 12)
        output = TestRectangle__str__.stdout_buffer(r)
        self.assertEqual(output.getvalue(), "[Rectangle] (12) 2/1 - 4/6\n")

    def test_str_method_width_height_x(self):
        r = Rectangle(5, 5, 1)
        correct = "[Rectangle] ({}) 1/0 - 5/5".format(r.id)
        self.assertEqual(correct, r.__str__())

    def test_str_method_width_height_x_y(self):
        r = Rectangle(1, 8, 2, 4)
        correct = "[Rectangle] ({}) 2/4 - 1/8".format(r.id)
        self.assertEqual(correct, str(r))

    def test_str_method_width_height_x_y_id(self):
        r = Rectangle(13, 21, 2, 4, 7)
        self.assertEqual("[Rectangle] (7) 2/4 - 13/21", str(r))

    def test_str_method_changed_attributes(self):
        r = Rectangle(7, 7, 0, 0, [4])
        r.width = 15
        r.height = 1
        r.x = 8
        r.y = 10
        self.assertEqual("[Rectangle] ([4]) 8/10 - 15/1", str(r))
    
    def test_str_method_one_arg(self):
        r = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaises(TypeError):
            r.__str__(1)

if __name__ == "__main__":
    unittest.main()

