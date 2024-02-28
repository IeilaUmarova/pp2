import re
word = str(input("Enter word: "))
print(re.findall(r'[a][a-z]+[b]', word))