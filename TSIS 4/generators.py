#1
n = int(input("Enter an input N: "))
a = (i**2 for i in range (1,n))
for i in a:
    print(i)

#2
n = int(input("Enter n: "))
for i in range (0, n+1, 2):
    if i<n:
     print(i, end = ',')
    else:
        print(i)

#3
def div_by_3and4(n):
    for i in range (0, n+1):
     if i%3==0 and i%4==0:
        print(i)

div_by_3and4(n=int(input("Enter n: ")))

#4
def squares():
    i=1
    while True:
        yield i*i
        i+=1
n = int(input("Enter a n: "))
for nums in squares():
    if nums>n:
        break
    print(nums)

#5
n=int(input("Enter n: "))
for i in range (n, -1, -1):
    print (i)