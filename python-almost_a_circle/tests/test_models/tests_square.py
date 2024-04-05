# test_square.py

import unittest
from models.square import Square
import json
import os


class TestSquare(unittest.TestCase):
    def test_square(self):
        s1 = Square(1, 2)
        self.assertEqual(s1.size, 1)
        self.assertEqual(s1.x, 2)

        s2 = Square(10, 2, 0)
        self.assertEqual(s2.size, 10)
        self.assertEqual(s2.x, 2)
        self.assertEqual(s2.y, 0)

        s3 = Square(10, 2, 0, 0)
        self.assertEqual(s3.size, 10)
        self.assertEqual(s3.x, 2)
        self.assertEqual(s3.y, 0)
        self.assertEqual(s3.id, 0)

        with self.assertRaises(TypeError):
            s4 = Square("1", 2)

        with self.assertRaises(TypeError):
            s5 = Square(1, "2")

        with self.assertRaises(TypeError):
            s6 = Square(1, 2, "3")

        s1 = Square(10, 2, 0, 12)
        self.assertEqual(s1.size, 10)
        self.assertEqual(s1.x, 2)
        self.assertEqual(s1.y, 0)
        self.assertEqual(s1.id, 12)

        with self.assertRaises(ValueError):
            s9 = Square(-1, 2)

        with self.assertRaises(ValueError):
            s10 = Square(1, -2)

        with self.assertRaises(ValueError):
            s11 = Square(0, 2)

        with self.assertRaises(ValueError):
            s12 = Square(1, 2, -3)

        s9 = Square(1)
        self.assertEqual(s9.size, 1)

    def test_str(self):
        """Test the string method"""
        s1 = Square(3, 1, 3, 4)
        self.assertEqual(s1.__str__(), "[Square] (4) 1/3 - 3")

    def test_to_dictionary(self):
        s1 = Square(10, 2, 1, 9)
        expected_output = {'x': 2, 'y': 1, 'id': 9, 'size': 10}
        self.assertEqual(s1.to_dictionary(), expected_output)

    def test_update(self):
        s1 = Square(10, 2, 1, 9)

        # Test update with positional arguments
        s1.update(20, 3, 2, 8)
        self.assertEqual(s1.id, 20)
        self.assertEqual(s1.size, 3)
        self.assertEqual(s1.x, 2)
        self.assertEqual(s1.y, 8)

        # Test update with keyword arguments
        s1.update(id=30, size=4, x=3, y=7)
        self.assertEqual(s1.id, 30)
        self.assertEqual(s1.size, 4)
        self.assertEqual(s1.x, 3)
        self.assertEqual(s1.y, 7)

        # Test update with a mix of positional and keyword arguments
        # Positional arguments should take precedence
        s1.update(40, 5, x=6, y=14)
        self.assertEqual(s1.id, 40)
        self.assertEqual(s1.size, 5)
        # height should remain unchanged as it's not updated
        self.assertEqual(s1.x, 3)
        self.assertEqual(s1.y, 7)

    def test_create(self):
        s1 = Square(id=30, size=4, x=3, y=15)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual(s2.id, 30)
        self.assertEqual(s2.size, 4)
        self.assertEqual(s2.x, 3)
        self.assertEqual(s2.y, 15)

    def test_save_to_file(self):
        s1 = Square(10, 7, 2, 8)
        s2 = Square(2, 3, 4, 5)
        Square.save_to_file([s1, s2])
        with open("Square.json", "r") as file:
            output = json.load(file)
        expected_output = [s1.to_dictionary(), s2.to_dictionary()]
        self.assertEqual(output, expected_output)

        Square.save_to_file(None)
        with open("Square.json", "r") as file:
            output = json.load(file)
        expected_output = []
        self.assertEqual(output, expected_output)

    def test_load_from_file_none(self):
        list_square_input = None
        Square.save_to_file(list_square_input)
        Square.load_from_file()
        self.assertTrue(os.path.exists("Square.json"))