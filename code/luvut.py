print(range(10))
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 

print( [x**2 for x in range(11)] )
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

some_list = [1, 4, 7, 'foo', 12, 'bar']
print( [x for x in some_list if str(x).isalpha()] )
# ['foo', 'bar']

print(  # Alkulukuja 
  [x for x in range(2, 50) if all([x % y for y in range(2, x-1)])] 
)
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

