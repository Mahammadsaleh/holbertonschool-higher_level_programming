#!/usr/bin/python3
""" Doc """


from models.rectangle import Rectangle


class Square(Rectangle):
    """Square"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y)

    @property
    def size(self):
        return self.width  # Since width = height for a Square, we can return either

    @size.setter
    def size(self, value):
        # Since a Square's width and height are always equal, setting size should update both
        self.width = value
        self.height = value
    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x,
                                                 self.y,
                                                 self.width)
