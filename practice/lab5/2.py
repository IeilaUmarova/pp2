import re
word = str(input("Enter word: "))
print(re.findall("ab{2,3}", word))