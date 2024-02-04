#!/usr/bin/python3                                                                                    """documentation"""
"""documentation"""


class Square:
    """Square class with private attribute size"""
    def __init__(self, size=0, position=(0, 0)) -> None:
        """Initialize Square with size attribute"""
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @property
    def position(self):
        return self.__position

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @position.setter
    def position(self, value):
        if not isinstance(list(self.__position)[0], int) or \
                not isinstance(list(self.__position)[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Public instance method return Size
        """
        return self.__size ** 2

    def my_print(self):
        """Public instance method return Size
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
