# test_base.py

import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    
    def test_id_is_not_none(self):
        test1 = Base(12)
        self.assertEqual(test1.id, 12)
        
    def test_id_is_none(self):
        test2 = Base()
        test3 = Base()
        test4 = Base()
        self.assertEqual(test2.id, 1)
        self.assertEqual(test3.id, 2)
        self.assertEqual(test4.id, 3)
        
    def test_to_json_string(self):
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string([{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]),
                         '[{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]')
        
    def test_from_json_string(self):
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string([]), [])
        self.assertEqual(Base.from_json_string('[{"id": 89, "width": 10, "height": 4}, {"id": 7, "width": 1, "height": 7}]'),
                                               [{"id": 89, "width": 10, "height": 4}, {"id": 7, "width": 1, "height": 7}])
        
        


    