#!/usr/bin/python3
"""Unittest for Almost a circle project"""

import unittest
import json
import sys
import os
import io

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestRectangle(unittest.TestCase):
    """Unittest for Rectangle class"""
    def test_init(self):
        rectangle = Rectangle(1, 2)
        self.assertEqual(rectangle.width, 1)
        self.assertEqual(rectangle.height, 2)
       
        rectangle1 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(rectangle1.width, 1)
        self.assertEqual(rectangle1.height, 2)
        self.assertEqual(rectangle1.x, 3)
        self.assertEqual(rectangle1.y, 4)
        self.assertEqual(rectangle1.id, 5)
       
    def test_types(self):
        """Test the type of arguments passed to the class"""
        with self.assertRaises(TypeError):
            Rectangle("1", 2)
        with self.assertRaises(TypeError):
            Rectangle(1, "2")
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3")
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "5")
   
    def test_values(self):
        """Test the values of arguments passed to the class"""
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)
        with self.assertRaises(ValueError):
            Rectangle(1, -2)
        with self.assertRaises(ValueError):
            Rectangle(0, 2)
        with self.assertRaises(ValueError):
            Rectangle(1, 0)
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3)
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -4)

    def test_area(self):
        """Test the value of the area"""
        rectangle = Rectangle(3, 4)
        self.assertEqual(rectangle.area(), 12)

    def test_string_representation(self):
        """Test the string representation of a rectangle"""
        rectangle = Rectangle(3, 4, 1, 2, 5)
        self.assertEqual(str(rectangle), "[Rectangle] (5) 1/2 - 3/4")

    def test_display(self):
        """Test the output when diplaying a rectangle"""
        rectangle = Rectangle(2, 3)
        actual_output = io.StringIO()
        sys.stdout = actual_output
        rectangle.display()
        printed_output = actual_output.getvalue()
        sys.stdout = sys.__stdout__
        expected_output = "##\n##\n##\n"
        self.assertEqual(printed_output, expected_output)
       
        rectangle = Rectangle(2, 3, 1, 1)
        actual_output = io.StringIO()
        sys.stdout = actual_output
        rectangle.display()
        printed_output = actual_output.getvalue()
        sys.stdout = sys.__stdout__
        expected_output = "\n ##\n ##\n ##\n"
        self.assertEqual(printed_output, expected_output)

    def test_to_dictionary(self):
        """Test the dictionary representation of a rectangle"""
        rectangle = Rectangle(3, 4, 1, 2, 5)
        self.assertEqual(rectangle.to_dictionary(), {'x': 1, 'y': 2, 'id': 5, 'width': 3, 'height': 4})

    def test_update(self):
        """Test when updating the value of a rectangle"""
        rectangle = Rectangle(1, 2)
        rectangle.update(2, 3, 4, 5, 6)
        self.assertEqual(rectangle.id, 2)
        self.assertEqual(rectangle.width, 3)
        self.assertEqual(rectangle.height, 4)
        self.assertEqual(rectangle.x, 5)
        self.assertEqual(rectangle.y, 6)

    def test_update_method_exists(self):
        """Test that the class possess an update method"""
        rectangle = Rectangle(1, 2)
        self.assertTrue(hasattr(rectangle, 'update'))

    def test_create_method_exists(self):
        """Test that the class possess a create method"""
        rectangle = Rectangle.create(**{'id': 89, 'width': 1})
        self.assertTrue(hasattr(rectangle, 'create'))

    def test_save_to_file_with_none(self):
        """Test if the save_to_file method works with a None argument"""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            dict_output = json.load(f)
        expected_output = []
        self.assertEqual(dict_output, expected_output)

if __name__ == "__main__":
    unittest.main()
