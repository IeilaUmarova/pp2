import os
path = '/Users/leila/Desktop/pp2_Leila_Umarova/practice/lab6/dir and files/file_4.txt'
if os.path.exists(path):
    os.remove(path)
    print("File has been removed")
else:
    print('Path does not exist')