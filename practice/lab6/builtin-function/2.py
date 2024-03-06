text = input()
upper = 0
lower = 0
for i in text:
    if i.isupper():
        upper+=1
    elif i.islower():
        lower+=1
print("Number of uppercase letter: ", upper)
print("Number of lowercase letter: ", lower)