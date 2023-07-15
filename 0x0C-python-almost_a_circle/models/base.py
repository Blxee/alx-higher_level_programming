#!/usr/bin/python3
"""Module for the ``Base`` class"""
import json
import os


class Base:
    """
    Base class is the base of all classes in this project
    Attributes:
        id (int): the isntance id
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns the json representation of list_dictionaries
        Args:
            list_dictionaries (list[dict]): a list of dicts
        Returns:
            a json string representation of ``list_dictionaries``
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return '[]'
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        saves a list of instances that inherit from ``Base`` as json
        Args:
            list_objs (list): list of instances
        """
        file_name = cls.__name__ + '.json'
        data = Base.to_json_string([obj.to_dictionary() for obj in list_objs])
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(data)

    @staticmethod
    def from_json_string(json_string):
        """
        parses a json string to a list of dictionaries
        Args:
            json_string (str): the target json string
        Returns:
            a list of dictionaries or an emptt list
        """
        if not json_string:
            return []
        list_dictionaries = json.loads(json_string)
        return list_dictionaries

    @classmethod
    def create(cls, **dictionary):
        """
        create an instance of subclass from dictionary of data
        Args:
            **dictionary: keyword arguments representing the data
        Returns:
            new instance of a child class
        """
        instance = cls(1, 1)
        instance.update(**dictionary)
        return instance

    @classmethod
    def load_from_file(cls):
        """
        loads a json file and creates a list of instances
        Returns:
            list of ``Base`` subclasses instances
        """
        file_name = cls.__name__ + '.json'
        if not os.path.isfile(file_name):
            return []
        json_string = None
        with open(file_name, 'r', encoding='utf-8') as file:
            json_string = file.read()
        list_dictionaries = cls.from_json_string(json_string)
        list_objs = [cls.create(**dict) for dict in list_dictionaries]
        return list_objs
