import functools

class a: 
  def out(text):
    print(text)

for x in 'Hello World':
  a.a = functools.partial(a.out, a, x)
  a.a()

