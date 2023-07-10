#!/usr/bin/python3
"""Module for Square class"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class that defines a square which inhirits from Rectangle"""

    def __init__(self, size):
        self.integer_validate('size', size)
        self.__width = self.__height = self.__size = size
