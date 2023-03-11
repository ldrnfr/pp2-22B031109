#1
from functools import reduce

list = [1,2,3,5,6]

result = reduce(lambda x, y: x * y, list)

print(result)

#2
string = "Norman Fucking Rockwell"

upper_count = sum(1 for letter in string if letter.isupper())
lower_count = sum(1 for letter in string if letter.islower())

print("Number of upper case letters: ",upper_count)
print("Number of lower case letters: ",lower_count)


#3
string = "poop"

if string == string[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")

#4
import math
import time

num = 25100
delay = 2123 / 1000

time.sleep(delay)

result = math.sqrt(num)

print(f"Square root of {num} after {delay} miliseconds is {result}")

#5

my_tuple = (True, True, False, True)

if all(my_tuple):
    print("All elements are true")
else:
    print("Not all elements are true")

