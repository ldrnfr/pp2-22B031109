#1
def to_ounces(grams):
    return grams*28.3495231
ingredient = to_ounces(35)
print(ingredient) #try it with input number 
#2
def to_celcium(farenheit):
    return (farenheit-32)*(5/9)
degree = to_celcium(56)
print(degree)#try it with input number
#3
def solve(numheads,numlegs):
    chicken_count=0
    rabbit_count=0

    if(numheads>=numlegs):
        print("No solution")
    elif(numlegs%2!=0):
        print("No solution")
    else:
        chicken_count=(numlegs/2)-numheads
        rabbit_count= numheads-chicken_count
        print(int(chicken_count), int(rabbit_count))

solve(35, 94)  
#4
input_string=input()
user_list=input_string.split()
for i in range (len(user_list)):
    user_list[i]=int(user_list[i])
def filter_prime(user_list):
    for i in range (2,(len(user_list/2)+1)):
        if user_list[i]%i!=0:
            return filter(user_list[i])
#5
import itertools
if __name__=='__main__':
    string = input()
    num = list(string)
    permutations=list(itertools.permutations(num))
    print([''.join(permutation) for permuatation in permutations])
#6
def reverse_sentence(string):
    split_string= string.split(' ')
    reversed_string=reversed(split_string) #applicable for string etc.
    final_string=' '.join(reversed_string)
    print(final_string)
sentence1 = reverse_sentence(input())
#7
def has_33nums(nums):
    for i in range(len(nums-1)):
        if nums[i]==2:
            if nums[i]==nums[i+1]:
                return True
            else:
                return False
nums_string=input()
nums = nums_string.split()
for i in range(len(nums)):
    nums[i] = int(nums[i])
ex = has_33nums(nums_string)
#8
def spy_game(nums):
    for i in range(0,len(nums)):
        if nums[i] == 0:
            for x in range(i+1,len(nums)):
                if nums[x] == 0:
                    for y in range(x+1,len(nums)):
                        if nums[y] == 7:
                            return True
                else:
                    return False 
print(spy_game([1,2,4,0,0,7,5])) # True
print(spy_game([1,0,2,4,0,5,7])) # True
print(spy_game([1,7,2,0,4,5,0])) # False
#9
import math
def sphere_volume(radius):
    return (radius**3)*math.pi*4/3
volume1 = sphere_volume(2)
print(volume1)
#10
def unique_list(list):
    x=[]
    for a in list:
     if a not in x:
        x.append(a)
    return x

print(unique_list([1,2,3,3,4,5,6,7,7,8,8]))

#11
def is_palindrome(string):
    left = 0
    right = len(string)-1
    while right>=left:
        if not string[left]==string[right]:
            return False
        left+=1
        right-=1
    return True
print(is_palindrome("madam"))
#12
def histogram(input_list):
    for i in range(len(input_list)):
        print (input_list[i]*'*')
List = [4, 9, 7]
histogram(List)
#13 #14
import random
guesses_taken = 0
print('Hello, what is your name?')
my_name=input()
number=random.randint(1,20) #random number between 1 and 20
print('Well,'+ my_name+', I am thinking of a number between 1 and 20.')
while guesses_taken <6:
    print('Take a guess.')
    guess = int(input())
    guesses_taken+=1
    if guess<number:
        print('Your guess is too low.')
    if guess>number:
        print('Your guess is too high.')
    if guess==number:
        break
if guess==number:
        print('Good job, ' + my_name + '! You guessed my number in ' + str(guesses_taken) + ' guesses!')
if guess !=number:
    number=str(number)
    print('Nope. The number I was thinking of was ' + number)
    


