import re
inp = input()
pattern = r'^[a-z]*_[a-z]*$'
result = bool(re.fullmatch(pattern, inp))
print(result)