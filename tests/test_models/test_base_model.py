#!/usr/bin/python3
"""module test_base_model"""
import unittest
import models
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """tests the class: BaseModel"""

    def test_init_id(self):
        """ tests the init method with id"""
        b1 = BaseModel()
        b2 = BaseModel(1)
        self.assertIsInstance(b1, BaseModel)
        self.assertTrue(hasattr(b1, "id"))
        self.assertNotEqual(b1.id, b2.id)
        self.assertIsInstance(b1.id, str)

    def test_init_attributes(self):
        """ tests the init method with created_at/updated_at attribute"""
        b1 = BaseModel(None)
        b1.name = "My First Model"
        b1.number = 89
        self.assertTrue(hasattr(b1, "created_at"))
        self.assertTrue(hasattr(b1, "updated_at"))
        self.assertTrue(hasattr(b1, "name"))
        self.assertTrue(hasattr(b1, "number"))
        self.assertIsInstance(b1.created_at, datetime)
        self.assertIsInstance(b1.updated_at, datetime)

    def test_init_kwargs(self):
        "test_init_kwargs tests kwargs if working correctrly"
        a_dict = {
                'id': '56d43177-cc5f-4d6c-a0c1-e167f8c27337',
                'created_at': '2017-09-28T21:03:54.052298',
                '__class__': 'BaseModel',
                'my_number': 89,
                'updated_at': '2017-09-28T21:03:54.052302',
                'name': 'My_First_Model'
                }
        bm1 = BaseModel(**a_dict)

        self.assertNotIn("__class__", bm1.__dict__)
        self.assertDictEqual(a_dict, bm1.to_dict())
        self.assertIsInstance(bm1.created_at, datetime)
        self.assertIsInstance(bm1.updated_at, datetime)

    def test_init_kwargs_empty(self):
        "test_init_kwargs_ tests kwargs if working correctrly if empty"
        self.assertIn(BaseModel(), models.storage.all().values())

    def test_to_dict_type(self):
        "test_to_dict_type tests if working correctrly"
        bm1 = BaseModel()
        json_bm1 = bm1.to_dict()

        self.assertIsInstance(json_bm1, dict)
        for k in json_bm1.keys():
            self.assertIsInstance(json_bm1[k], str)

    def test_to_dict_difference(self):
        "test_to_dict_difference tests if working correctrly"
        bm = BaseModel()
        self.assertNotEqual(bm.__dict__, bm.to_dict())

    def test_to_dict_attributes(self):
        "test_to_dict_attributes tests if working correctrly"
        bm = BaseModel()
        bm.name = "model"
        bm.number = 89
        self.assertIn("__class__", bm.to_dict())
        self.assertIn("name", bm.to_dict())
        self.assertIn("number", bm.to_dict())

    def test_to_dict_args(self):
        "test_to_dict_args tests if working correctrly"
        bm = BaseModel()
        with self.assertRaises(TypeError):
            bm.to_dict(None)

    def test_save(self):
        "test_save tests if working correctrly"
        bm1 = BaseModel()
        bm1.save()
        self.assertNotEqual(bm1.created_at, bm1.updated_at)
if __name__ == "__main__":
    unittest.main()
