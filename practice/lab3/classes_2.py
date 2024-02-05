#1
class InputString :
    def __init__ (self):
        self.input_string = ""
    def getstring(self):
        self.input_string = input("Enter: ")
    def printstring (self):
        print(self.input_string.upper())

#2
class shape :
    def area(self):
        return 0;
class spuare(shape) :
    def __init__ (self, lenght):
        self.length = lenght
    def srea (self):
        return self.legth **2
    
#3
class rectangle(shape) :
    def __init__ (self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
    
#4
class point :
    def __init__ (self, x, y):
        self.x = x
        self.y = y
    def show(self):
        print(f"coordinates: ({self.x}, {self.y})")
    def move(self, x1, y1):
        self.x1 = x1
        self.y1 = y1
    def dist(self, point_1):
        return((self.x - point_1.x)**2 + (self.y - point_1.y)**2)**0,5
    