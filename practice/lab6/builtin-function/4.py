import time
num = int(input())
milsec = int(input())
sec = milsec/1000
time.sleep(sec)
sqrt = num ** 0.5
text = "Square root of"
text1 = "after"
text2 = "miliseconds is"
print(text, num, text1, sec, text2, sqrt)
