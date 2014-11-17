# -*- coding: utf-8 -*-

import __builtin__

def x(*args): 
  return args

print(x(1, 5, 'kissa'))
# (1, 5, 'kissa')

print(dir(__builtin__))
# ['ArithmeticError', 'AssertionError', 'AttributeError', ... ]

__builtin__.dir = x

print(dir(__builtin__))
# (<module '__builtin__' (built-in)>,)

