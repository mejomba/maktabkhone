import re
pattern = r"^\w+@[a-zA-Z]+\.[a-zA-z]+$"
mail = input()
if not re.match(pattern, mail):
    print('WRONG')
else:
    print('OK')