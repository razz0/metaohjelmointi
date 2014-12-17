import __builtin__

def x(*args): 
  return args

print(dir(__builtin__))
# ['ArithmeticError', 'AssertionError', ... ]

__builtin__.dir = x

print(dir(__builtin__))
# (<module '__builtin__' (built-in)>,)

