#1
import math
degree = float(input("Input degrees: "))
radian = math.radians(degree)
print(f"Output radians: {radian} ")

#2
import math
height = int(input("Height: "))
base1 = int(input("Base, first value: "))
base2 = int(input("Base, second value: "))
area = ((base1+base2)/2)*height
print(f"Area: {area}")

#3
#the area and conditions of regular polygon changes with the n>=3 and <=8
import math
n = int(input("Input number of sides: "))
length = int(input("Input the length of a side: "))
if n==4:
    area = length*length 
if n==3:
    area = (math.sqrt(3)/4)*(length*length)
if n==5:
    area = 1/2*(length/2*math.tan(180/n))*(length*n)
if n==6:
    area = (3*math.sqrt(3)*length*length)/2
if n==7:
    area = 7/4*(length*length*math.cos(math.pi/7))
if n==8:
    area = 2*(1+math.sqrt(2))*length*length
print(area)

#4
import math
length = float(input("Length of base: "))
height = float(input("Height of a parallelogram: "))
area = length*height
print(f"Area: {area}")
