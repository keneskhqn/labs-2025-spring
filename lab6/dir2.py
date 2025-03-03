import os 

file_name = r"C:\Users\User\Desktop\pythonkbtu\labs-2025-spring\test.txt"

print(os.access(file_name, os.F_OK)) 
print(os.access(file_name, os.R_OK)) 
print(os.access(file_name, os.W_OK)) 
print(os.access(file_name, os.X_OK))