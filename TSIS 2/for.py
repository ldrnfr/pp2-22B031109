fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x) #1

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":  
   continue
  print(x) #2


for x in range(6):
  print(x) #3

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":  
   break
  print(x) #4

