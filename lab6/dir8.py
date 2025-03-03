import os

cf = r"C:\Users\User\Desktop\pythonkbtu\labs-2025-spring\lab6\A.txt"

if os.path.exists(cf) and os.access(cf, os.W_OK): 
    if os.path.isfile(cf): 
        os.remove(cf)  
        print("file deleted")
    else:
        print("this path is not a file")
else:
    print("file doesn't exist")

