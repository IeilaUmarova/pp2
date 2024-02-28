import re
word = str(input("Enter word: "))
print(re.findall(r'[A-Z]{1}[a-z]+', word))