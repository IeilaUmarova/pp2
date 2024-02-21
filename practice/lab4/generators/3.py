def generator3_4(n):
    for i in range(n+1):
        if i%3==0 and i%4==0:
            yield i
for i in generator3_4(40):
    print(i)