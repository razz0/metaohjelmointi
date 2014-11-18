code_str = 'print("Hello world!")'
code_obj = compile(code_str, '<string>', 'single')

print(code_obj)
# <code object <module> at 0x7f06341f2cb0, file "<string>", line 1>

exec(code_obj)
# Hello world!
