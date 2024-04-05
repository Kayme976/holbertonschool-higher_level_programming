# test_rectangle.py

import unittest
from models.rectangle import Rectangle
from io import StringIO
import sys
import json
import os


class TestRectangle(unittest.TestCase):

    def test_rectangle(self):
        """Test the creation of a Rectangle object."""
        r1 = Rectangle(1, 2)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)

        r2 = Rectangle(10, 2, 0)
        self.assertEqual(r2.width, 10)
        self.assertEqual(r2.height, 2)
        self.assertEqual(r2.x, 0)

        r3 = Rectangle(10, 2, 0, 0)
        self.assertEqual(r3.width, 10)
        self.assertEqual(r3.height, 2)
        self.assertEqual(r3.x, 0)
        self.assertEqual(r3.y, 0)

        with self.assertRaises(TypeError):
            r4 = Rectangle("1", 2)

        with self.assertRaises(TypeError):
            r5 = Rectangle(1, "2")

        with self.assertRaises(TypeError):
            r6 = Rectangle(1, 2, "3")

        with self.assertRaises(TypeError):
            r7 = Rectangle(1, 2, 3, "4")

        r8 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r8.width, 10)
        self.assertEqual(r8.height, 2)
        self.assertEqual(r8.x, 0)
        self.assertEqual(r8.y, 0)
        self.assertEqual(r8.id, 12)

        with self.assertRaises(ValueError):
            r9 = Rectangle(-1, 2)

        with self.assertRaises(ValueError):
            r10 = Rectangle(1, -2)

        with self.assertRaises(ValueError):
            r11 = Rectangle(0, 2)

        with self.assertRaises(ValueError):
            r11 = Rectangle(1, 0)

        with self.assertRaises(ValueError):
            r12 = Rectangle(1, 2, -3)

        with self.assertRaises(ValueError):
            r13 = Rectangle(1, 2, 3, -4)

    def test_area(self):
        """Test the area calculation of a Rectangle object."""
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)
        r2 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r2.area(), 56)

    def test_str(self):
        """Test the string method"""
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(r1.__str__(), "[Rectangle] (12) 2/1 - 4/6")

    def test_display(self):
        r1 = Rectangle(4, 6)
        buffer = StringIO()
        sys.stdout = buffer
        r1.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(buffer.getvalue(),
                         "####\n####\n####\n####\n####\n####\n")

        r2 = Rectangle(4, 6, 5, 3)
        buffer = StringIO()
        sys.stdout = buffer
        r2.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(buffer.getvalue(
        ), "\n\n\n     ####\n     ####\n     ####\n     ####\n     ####\n     ####\n")

    def test_to_dictionary(self):
        r1 = Rectangle(10, 2, 1, 9, 17)
        expected_output = {'x': 1, 'y': 9, 'id': 17, 'height': 2, 'width': 10}
        self.assertEqual(r1.to_dictionary(), expected_output)

    def test_update(self):
        r1 = Rectangle(10, 2, 1, 9, 17)

    # Test update with positional arguments
        r1.update(20, 3, 2, 8, 16)
        self.assertEqual(r1.id, 20)
        self.assertEqual(r1.width, 3)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 8)
        self.assertEqual(r1.y, 16)

    # Test update with keyword arguments
        r1.update(id=30, width=4, height=3, x=7, y=15)
        self.assertEqual(r1.id, 30)
        self.assertEqual(r1.width, 4)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 7)
        self.assertEqual(r1.y, 15)

    # Test update with a mix of positional and keyword arguments
    # Positional arguments should take precedence
        r1.update(40, 5, x=6, y=14)
        self.assertEqual(r1.id, 40)
        self.assertEqual(r1.width, 5)
    # height should remain unchanged as it's not updated
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 7)
        self.assertEqual(r1.y, 15)

    def test_create(self):
        r1 = Rectangle(id=30, width=4, height=3, x=7, y=15)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(r2.id, 30)
        self.assertEqual(r2.width, 4)
        self.assertEqual(r2.height, 3)
        self.assertEqual(r2.x, 7)
        self.assertEqual(r2.y, 15)

    def test_save_to_file(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 3, 4, 5, 6)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
            output = json.load(file)
        expected_output = [r1.to_dictionary(), r2.to_dictionary()]
        self.assertEqual(output, expected_output)

        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            output = json.load(file)
        expected_output = []
        self.assertEqual(output, expected_output)

    def test_load_from_file_none(self):
        list_rectangles_input = None
        Rectangle.save_to_file(list_rectangles_input)
        Rectangle.load_from_file()
        self.assertTrue(os.path.exists("Rectangle.json"))