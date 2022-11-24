#!/usr/bin/python3
'''Creating an empty class'''
class Square:
    pass

class Square:
    _size = int
    def __init__(self, size = 0):
        if type(size) != int:
            raise TypeError("Size must be an integers")
        if size < 0:
            raise TypeError("Size must be >= 0")
        self._size = size
    def area(self):
        return self._size ** 2

a = Square(10)
a.area()


    