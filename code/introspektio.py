# -*- coding: utf-8 -*-

a = 42

print(type(a))
# <type 'int'>

print(dir(a))
# ['__abs__', '__add__', '__and__', '__class__', '__cmp__', ... ] 

print(a.__doc__)
# int(x[, base]) -> integer
# ...

print(a.bit_length.__doc__)
# int.bit_length() -> int
# ...

