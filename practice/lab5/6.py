import re
word = str(input("Enter word: "))
words = re.sub(r'[^\w\s]',' ', word)
print(re.sub(" ", ":", words))