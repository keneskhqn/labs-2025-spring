file_name = r"C:\Users\User\Desktop\pythonkbtu\labs-2025-spring\test.txt"  

with open(file_name, 'r') as file:
    summ = sum(1 for i in file)

print(f"Number of lines: {summ}")