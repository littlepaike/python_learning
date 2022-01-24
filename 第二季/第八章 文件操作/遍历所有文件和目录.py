import os

path = os.getcwd()
list_files = os.walk(path)
for dirpath, dirnames, filenames in list_files:
    for dir in dirnames:
        print(os.path.join(dirpath, dir))
    for file in filenames:
        print(os.path.join(dirpath, file))