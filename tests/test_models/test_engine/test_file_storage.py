#!/usr/bin/python3
"""Module test_file_storage"""
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review


class TestFileStorage(unittest.TestCase):
    """Tests class: FileStorage"""

    def test_init(self):
        "test_init if it works"
        storage = FileStorage()
        self.assertIsInstance(FileStorage(), FileStorage)
        self.assertTrue(hasattr(storage, '_FileStorage__objects'))
        self.assertTrue(hasattr(storage, '_FileStorage__file_path'))
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))
        with self.assertRaises(TypeError):
            FileStorage(None)
if __name__ == "__main__":
    unittest.main()
