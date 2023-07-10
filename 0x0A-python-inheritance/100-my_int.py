#!/usr/bin/python3
"""Module for ``MyInt`` class"""


class MyInt(int):
    """Class that defines MyInt which inherits from int"""

    def __eq__(self, x):
        return super().__nq__(x)

    def __nq__(self, x):
        return super().__eq__(x)
