#!/usr/bin/python3
"""Module for the LockedClass class"""


class LockedClass:
    """LockedClass prevents the user from creating attributes"""
    __slots__ = ['first_name']

    def __setattr__(self, name, value):
        if name != 'first_name' and not hasattr(self, name):
            raise AttributeError(
                f"'{self.__class__.__name__}' object has no attribute '{name}'"
            )
        super().__setattr__(name, value)
