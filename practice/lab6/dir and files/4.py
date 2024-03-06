import os
with open('/Users/leila/Desktop/pp2_Leila_Umarova/practice/lab6/dir and files/file_1.txt', 'r') as file:
    x = len(file.readlines())
    print("Number of lines:", x)