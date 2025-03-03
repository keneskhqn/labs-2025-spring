import os
copyf = r"C:\Users\User\Desktop\pythonkbtu\labs-2025-spring\test.txt"
copiedf = r"C:\Users\User\Desktop\pythonkbtu\labs-2025-spring\lab6\A.txt"
try:
    with open(copyf, 'r') as src, open(copiedf, 'w') as dest:
        content = src.read()
        dest.write(content)
except Exception as e:
    print(f"An error occurred: {e}")