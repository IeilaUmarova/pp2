import os
mylist = ['A', 'B', 'C', 'D']
with open('/Users/leila/Desktop/pp2_Leila_Umarova/practice/lab6/dir and files/file_2.txt', 'w') as file:
    for i in mylist:
        file.write(i + '\n')