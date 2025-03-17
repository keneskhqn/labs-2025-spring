import re
inp = input()
pattern = r'^a*b*$'
result = bool(re.fullmatch(pattern, inp))
print(result)