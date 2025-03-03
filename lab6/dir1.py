import os
path= r"C:\Program Files (x86)\Apple Software Update"

result = os.listdir(path)
for i in result:
    print(i)