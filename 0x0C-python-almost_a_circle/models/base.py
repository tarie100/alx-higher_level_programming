#!/usr/bin/python3
"""define class"""

class Base:
    __nb_objects = 0  # Private class attribute

    def __init__(self, id=None):
        """initialize"""
        if id is not None:
            self.id = id  # Assign the public instance attribute 'id' with the argument value
        else:
            Base.__nb_objects += 1  # Increment __nb_objects
            self.id = Base.__nb_objects  # Assign the new value to 'id'
