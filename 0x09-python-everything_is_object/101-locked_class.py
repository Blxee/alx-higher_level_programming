#!/usr/bin/python3
"""Module for the LockedClass class"""


class LockedClass:
    """LockedClass prevents the user from creating attributes"""

    def __setattr__(self, name, value):
        if name == 'first_name' and type(value) == str:
            super().__setattr__(name, value)
        else:
            raise AttributeError(
                f"'{self.__class__.__name__}' object has no attribute '{name}'"
            )
