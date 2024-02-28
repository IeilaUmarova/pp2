import re
word = str(input("Enter word: "))
print(re.findall(r'[a-z]+[_][a-z]+', word))