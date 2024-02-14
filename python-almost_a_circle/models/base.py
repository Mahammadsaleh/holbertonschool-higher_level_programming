#!/usr/bin/python3
"""Documentation"""


import json


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Documentation of to_json_string"""

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation"""

        file = f"{cls.__name__}.json"

        with open(file, mode="w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                lst = [e.to_dictionary() for e in list_objs]
                f.write(cls.to_json_string(lst))
