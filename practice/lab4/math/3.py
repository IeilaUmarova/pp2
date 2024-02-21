import math
n = int(input("Input number of sides: "))
l = float(input("Input the length of a side: "))
S = (n*l**2)/(4*math.tan(math.pi/n))
s = round(S)
print("The area of the polygon is: ", s)