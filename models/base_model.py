#!/usr/bin/python3
"""this module defines the class: BaseModel
"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """This is the class BaseModel
    """

    def __init__(self, *args, **kwargs):
        """Initiliaze an instance:
        Args:
        id (str): assign with an uuid when an instance is created
        created_at (datetime): the current datetime when an instance is created
        updated_at (datetime): the current datetime when an instance is created
                               it will be updated when an obj is changed
        *args: (unused)
        **kwargs (dict): key/pair value of the instance's attributes
        """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        timeform = "%Y-%m-%dT%H:%M:%S.%f"

        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, timeform)
                elif k == "__class__":
                    continue
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def __str__(self):
        """It prints: [<class name>] (<self.id>) <self.__dict__>
        """
        classe_name = type(self).__name__
        return "[{}] ({}) {}".format(classe_name, self.id, self.__dict__)

    def save(self):
        """Updates the public instance attribute updated_at
        with the current datetime
        """

        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of:
        __dict__ of the instance
        a key: __class__ is added with the class name of the object
        """
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        return obj_dict
