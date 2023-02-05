#1
class String():
    def __init__(self):
        self.str = ""

    def getString(self):
        self.str = input()

    def printString(self):
        print(self.str.upper())

str1 = String()
str1.getString()
str1.printString()
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
print(Figure2.Area()) 
#4
import math
class Point():
    def __init__(self, x, y):
        self.x = int(input(x))
        self.y = int(input(y))
    def Show(self):
        return self.x, self.y
    def Move(self, x, y):
        self.x +=x
        self.y +=y
    def Dist(self, pt):
        dis_x = pt - self.x # pt is x2 and x is x1
        dis_y = pt - self.y # pt is y2 and y is y1
        return math.sqrt(dis_x**2 + dis_y**2)

p1=Point(2,3)
p2=Point(3,5)
p1.Show()
p2.Show()

#5
class Account():
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def __str__(self):
        return f'Account owner: {self.owner} \nAccount balance: ${self.balance}'
    def Deposit(self, dep_amount):
        self.balance += dep_amount
        print("Deposit is added to the balance")
    def Withdrawal(self, withd_amount):
        if self.balance>=withd_amount:
            self.balance-=withd_amount
            print("Withdrawal is removed from the balance")
        else:
            print("Not enough money")
client = Account('Aruzhan', 1000000)
print(client)
client.Deposit(50)
print(client)
client.Withdrawal(50)
print(client)
#6
input_string = input('elements separated by a space')
user_list  = input_string.split()
print('list: ', user_list)
for i in range(len(user_list)):
    user_list[i]=int(user_list[i])
print("Prime numbers:")
prime_nums=list(filter(lambda x: all(x%i !=0 for i in range(2,int(x/2)+1)), user_list))
print(prime_nums)









