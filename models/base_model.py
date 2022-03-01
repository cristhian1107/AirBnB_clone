#!/usr/bin/python3
""" Class
        a) BaseModel.
"""
import uuid
from datetime import datetime


class BaseModel:
    """ Class:
            BaseModel that defines all common attributes/methods
            for other classes.
    """

    def __init__(self):
        """ Construct (replace):
                BaseModel object.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """ Method (replace):
                Represents the class objects as a string in format.
            Return:
                String in  format '[<class name>] (<self.id>) <self.__dict__>'.
        """
        class_str = ""
        class_str += "[" + self.__class__.__name__ + "] "
        class_str += "(" + self.id + ") "
        # note! : need to implement
        class_str += str(self.__dict__)
        return class_str

    def save(self):
        """ Method:
                Update auditory date and save change.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ Method:
                Generate dictionary of the class.
            Return:
                A dictionary containing all keys/values
                of __dict__ of the instance.
        """
        class_dict = dict()
        for key, value in self.__dict__.items():
            if key in ["created_at", "updated_at"]:
                class_dict[key] = value.isoformat()
            elif value:
                class_dict[key] = value
        class_dict["__class__"] = self.__class__.__name__
        return class_dict
