import re
word = str(input("Enter word: "))
print(re.findall("ab*", word))