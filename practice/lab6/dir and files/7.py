import os
with open('file_1.txt', 'r') as file1, open('file_3.txt', 'a') as file2:
    for line in file1:
        file2.write(line)