code_str = 'print("Hello world!")'
code_obj = compile(code_str, '<string>', 'single')

print(code_obj)
# <code object <module> ...

exec(code_obj)
# Hello world!
