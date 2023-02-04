#1
"""class String():
    def __init__(self):
        self.str = ""

    def getString(self):
        self.str = input()

    def printString(self):
        print(self.str.upper())

str1 = String()
str1.getString()
str1.printString()"""
#2
class Shape():
    def __init__(self):
        pass
    def Area(self):
        return 0
class Square(Shape):
    def __init__(self, length):
        Shape.__init__(self) #inheritance from Shape class
        self.length=length
    def Area(self):
        return self.length*self.length
Figure1 = Square(6)
print(Figure1.Area()) #retuen the area value
print(Shape().Area()) #prints 0 as it was initially set
#3
class Rectangle():
    def __init__(self, length, width):
        Shape.__init__(self)
        self.length = length
        self.width = width
    def Area(self):
        return self.length*self.width
Figure2 = Rectangle(5, 6)
print(Figure2.Area()) # returns the area of rectangle
#4
class Point():
    def __init__(self, x, y):
        self.x =x
        self.y = y
    def show(self):
        return self.x, self.y
    def move(self, x, y):
    def dist(self):


