#!/usr/bin/python3
"""A module that defines an Square class"""


class Square:
    """Class defines a square object
    Attributes:
        size (int, optional): size of the square
        position (:obj:`tuple`, optional): position of the square
    """

    def __init__(self, size=0, position=(0, 0)):
        """The class constructor
        Args:
            size (int, optional): size of the square
            position (:obj:`tuple`, optional): position of the square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter method for `size`"""
        return self.__size

    @size.setter
    def size(self, size=0):
        """Setter method for `size`
        Args:
            size (int, optional): size of the square
        """
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    @property
    def position(self):
        """Getter method for `position`"""
        return self.__position

    @position.setter
    def position(self, position=(0, 0)):
        """Setter method for `position`
        Args:
            position (:obj:`tuple`, optional): position of the square
        """
        self.__position = position

    def area(self):
        """Instance function for area of the square
        Returns:
            the area of the square (size ^ 2)
        """
        return self.__size ** 2

    def my_print(self):
        """Prints the square using the '#' character"""
        if self.size == 0:
            print()
            return
        for _ in range(self.position[1]):
            print()
        for _ in range(self.size):
            print(' ' * self.position[0], end='')
            print('#' * self.size)
