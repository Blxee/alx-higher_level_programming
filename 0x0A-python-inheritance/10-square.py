#!/usr/bin/python3
"""Module for Square class"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class that defines a square which inhirits from Rectangle"""

    def __init__(self, size):
        self.integer_validator('size', size)
        self.__size = size

    def area(self):
        """Calculates the area of the Square"""
        return self.__size ** 2

    def __str__(self):
        return f'[Rectangle] {self.__size}/{self.__size}'
