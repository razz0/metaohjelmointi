code_str = 'print("Hello world!")'
code_obj = compile(code_str, '<string>', 'single')

exec(code_obj)
# Hello world!
