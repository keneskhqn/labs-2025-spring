import re
inp = input()
pattern = r'^ab{2,3}$'
result = bool(re.fullmatch(pattern, inp))
print(result)