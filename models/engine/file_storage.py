#!/usr/bin/python3
""" module file_storage that defines class: FileStorage"""
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """serializes instances to a JSON file
    and deserializes JSON file to instances:
    Attributes:
    __file_path (str): path to the JSON file (file.json)
    __objects (dict): will store all objects by <class name>.id
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""

        # if len(self. __objects) != 0:
        serial_obj = {k: v.to_dict() for k, v in self.__objects.items()}
        with open(self.__file_path, "w") as f:
            str_to_json = json.dumps(serial_obj)
            f.write(str_to_json)

    def reload(self):
        """deserializes the JSON file to __objects if (__file_path) exists;
        otherwise, do nothing.
        """
        try:
            with open(self.__file_path, "r") as f:
                str_json = f.read()

        except FileNotFoundError:
            return

        if len(str_json) != 0:
            data = json.loads(str_json)
            for k, v in data.items():
                class_name, obj_id = k.split('.')
                class_ref = globals().get(class_name)
                self.__objects[k] = class_ref(**v)
