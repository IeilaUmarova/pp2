import os
from string import ascii_uppercase

for char in ascii_uppercase:
    file_path = '/Users/leila/Desktop/pp2_Leila_Umarova/practice/lab6/dir and files/{fchar}.txt'.format(fchar=char)
    open(file_path, 'x').close()