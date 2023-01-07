import re       
names = input()
names_list = re.split("\d+", names)
print(names_list)
