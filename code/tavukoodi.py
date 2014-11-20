# -*- coding: utf-8 -*-

import dis

def neliot(iteroitava):
  '''Palauta lista parametrin alkioiden neliöistä'''
  return [x**2 for x in iteroitava]
  
dis.dis(neliot)
#  4           0 BUILD_LIST               0
#              3 LOAD_FAST                0 (iteroitava)
#              6 GET_ITER            
#        >>    7 FOR_ITER                16 (to 26)
#             10 STORE_FAST               1 (x)
#             13 LOAD_FAST                1 (x)
#             16 LOAD_CONST               1 (2)
#             19 BINARY_POWER        
#             20 LIST_APPEND              2
#             23 JUMP_ABSOLUTE            7
#        >>   26 RETURN_VALUE        

