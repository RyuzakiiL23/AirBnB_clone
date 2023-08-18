#!/usr/bin/python3
"""module: test_place"""
import unittest
import os
import models
from datetime import datetime
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """Tests the class: Place"""

    def test_init(self):
        self.assertIsInstance(Place(), BaseModel)

    def test_init_id(self):
        """ tests the init method with id"""
        u1 = Place()
        u2 = Place(1)
        self.assertIsInstance(u2, Place)
        self.assertTrue(hasattr(u1, "id"))
        self.assertNotEqual(u1.id, u2.id)
        self.assertIsInstance(u1.id, str)

    def test_init_attributes(self):
        """ tests the init method with created_at/updated_at attribute"""
        u1 = Place()
        u2 = Place()
        self.assertTrue(hasattr(u1, "name"))
        self.assertTrue(hasattr(u1, "city_id"))
        self.assertTrue(hasattr(u1, "user_id"))
        self.assertIsInstance(u1.created_at, datetime)
        self.assertIsInstance(u1.updated_at, datetime)
        self.assertIsInstance(u1.city_id, str)
        self.assertIsInstance(u1.user_id, str)
        self.assertIsInstance(u1.name, str)
        self.assertIsInstance(u1.description, str)
        self.assertIsInstance(u1.number_rooms, int)
        self.assertIsInstance(u1.number_bathrooms, int)
        self.assertIsInstance(u1.max_guest, int)
        self.assertIsInstance(u1.price_by_night, int)
        self.assertIsInstance(u1.latitude, float)
        self.assertIsInstance(u1.longitude, float)
        self.assertIsInstance(u1.amenity_ids, list)
        self.assertNotEqual(u1.created_at, u2.created_at)
        self.assertNotEqual(u1.updated_at, u2.updated_at)

    def test_init_kwargs(self):
        a_dict = {
                'id': '56d43177-cc5f-4d6c-a0c1-e167f8c27337',
                'created_at': '2017-09-28T21:03:54.052298',
                '__class__': 'Place',
                'my_number': 89,
                'updated_at': '2017-09-28T21:03:54.052302',
                'name': 'view Hotel'
                }
        u = Place(**a_dict)
        self.assertNotIn("__class__", u.__dict__)
        self.assertDictEqual(a_dict, u.to_dict())
        self.assertIsInstance(u.created_at, datetime)
        self.assertIsInstance(u.updated_at, datetime)

    def test_init_kwargs_empty(self):
        "test_init_kwargs_ tests kwargs if working correctrly if empty"
        self.assertIn(Place(), models.storage.all().values())

    def test_to_dict(self):
        "test_to_dict_type tests if working correctrly"
        u = Place()
        json_u = u.to_dict()

        self.assertIsInstance(json_u, dict)
        for k in json_u.keys():
            self.assertIsInstance(json_u[k], str)

    def test_to_dict_difference(self):
        "test_to_dict_difference tests if working correctrly"
        u = Place()
        self.assertNotEqual(u.__dict__, u.to_dict())

    def test_to_dict_attributes(self):
        "test_to_dict_attributes tests if working correctrly"
        u = Place()
        self.assertNotIn("name", u.to_dict())
        u.name = "Lovely Beach"
        self.assertIn("__class__", u.to_dict())
        self.assertIn("name", u.to_dict())

    def test_to_dict_args(self):
        "test_to_dict_args tests if working correctrly"
        u = Place()
        with self.assertRaises(TypeError):
            u.to_dict(None)

    def test_save(self):
        "test_save tests if working correctrly"
        u = Place()
        u.save()
        self.assertNotEqual(u.created_at, u.updated_at)
        with self.assertRaises(TypeError):
            u.save(None)
if __name__ == "__main__":
    unittest.main()
