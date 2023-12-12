#!/usr/bin/python3

'''define a base module'''
import json


class Base:
    '''
    This Represents the "base" for all other classes in project 0x0C*.

    Private Class Attributes:
        __nb_object (int): Number of instantiated Bases.
    '''

    __nb_objects = 0

    def __init__(self, id=None):
        '''
      initialize a new base

      Args: id (int value)
        '''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects = Base.__nb_objects + 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of a list of dictionaries.

        Args:
            list_dictionaries (list): A list of dictionaries.

        Returns:
            str: The JSON string representation of the list of dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of a list of objects to a file.

        Args:
            list_objs (list): A list of objects that inherit from Base.
        """
        file = cls.__name__ + ".json"
        with open(file, "w") as jsfile:
            if list_objs is None:
                jsfile.write("[]")
            else:
                '''using to_dic method to represent obj in list as dic '''
            list_dicts = [obj.to_dictionary() for obj in list_objs]
            jsfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or len(json_string) == 0:
            return "[]"
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Creates an instance of all attributes set from a dictionary.

        Args:
            dictionary (dict): A dictionary containing attr

        Returns:
            Base: An instance of the class with all attributes set.
        """
        dummy = cls(1, 1, 1)
        '''to update args and kwargs provided in dummy'''
        dummy.update(**dictionary)
        return dummy
    @classmethod
    def load_from_file(cls):
        