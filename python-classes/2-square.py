#!/usr/bin/python3
"""This module contains an empty class Square that defines a square"""


class square:
   def __init__(self, size=0):
      if type(size) != int:
         raise TypeError("size must be an integer")
      elif size < 0:
         raise TypeError("size must be >= 0")
      else:
         self._size = size
