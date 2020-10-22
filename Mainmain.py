#%%
#Tuple
a_tuple = (57, "String", 57.0)
print(a_tuple[2])
#Can't .append or .pop with tuple

#%%
#List
a_list = [5, 2, 2, 2, 2, 2, "yes"]
a_list.append("no")
a_list.insert(0, "awal")
print(a_list)

i = 0
while True: 
    if i < a_list.count(2):
        a_list.remove(2)
    else:
        break
print(a_list)

#%%
#Guessing game, pick a number from 1 - 100. Program will tell if guess is too much or too little
import random
randomint = random.randint(1, 100)

print("Welcome to the guessing game! Pick a number from 1 - 100!")
while True:
    guess = int(input("Your guess: "))
    if guess == randomint:
        print("You guessed right! Congrats!")
        break
    elif guess > randomint:
        print("Too much! Try something less")
    elif guess < randomint:
        print("Too little! Try something more")

#%%
#Make inverse triangle from given height
TRIANGLE_HEIGHT = 5

for i in range(TRIANGLE_HEIGHT):
    print("*" * (i + 1))

for i in range(TRIANGLE_HEIGHT):
    print(" " * (TRIANGLE_HEIGHT - 1 - i) + "*" * (i + 1))

#%%
#Diamond assignment -> make diamond with "*" and " ", changing the width, height = (2 * width - 1)
#height di sini maksudnya cmn 1/2 tinggi fullnya sampe ke tengah
def diamond(height):
    for i in range(height):
        print(" " * (height - 1 - i) + "*" * (i * 2 + 1))   #Use + 1 because index only counts until height-1
    for i in range(height - 2, -1, -1):
        print(" " * (height - 1 - i) + "*" * (i * 2 + 1))

diamond(eval(input("Type the height you want: ")))
# More efficient version
def diamond1(height):
    for i in list(range(height)) + list(range(height - 2, -1, -1)):
        print(" " * (height - 1 - i) + "*" * (i * 2 + 1))

diamond1(eval(input("Type the height: ")))

#%%
#Make Empty Matrix
matrix_len = 5
matrix_height = 2

my_empty_matrix = [[0 for _ in range(matrix_len)] for _ in range(matrix_height)]
for vec in my_empty_matrix:
    print(vec)

def addition(a, b):
    result = a + b
    return result

my_var = addition(5, 6)
print(my_var)

#%%
def split_and_length(string):
    result1 = []
    for i in string:
        result1.append(i)
    return (result1, len(string))

my_var = "Jason"
chars, length = split_and_length(my_var)
print(chars)
print(length)

#%%
# class name always start with Capitalized letter
# class is like a blueprint
class Hammer:
    pass

my_hammer = Hammer()
# making an object from a class -> Instantiation
your_hammer = Hammer()
# now we have 2 objects
#%%
class Hammer:

    def __init__(self, mat):
        self.material = mat

    def print_hammer(self):
        print("Hello! I am made from " + self.material)

my_hammer = Hammer("Titanium")
your_hammer = Hammer("Iron")

# Calling methods -> Func in class
your_hammer.print_hammer()

# Getting attributes -> Var in class
print(your_hammer.material)

#%%
class Rectangle:

    def __init__(self, length):
        self.length = length
    
    def area(self):
        return self.length ** 2

rect = Rectangle(5)
print(rect.area())

#%%
class Triangle:

    def __init__(self, height, length):
        self.height = height
        self.length = length

    def area(self):
        return 1/2 * self.height * self.length

tri = Triangle(6, 3)
print(tri.area())

#%%
from functools import reduce

fib = lambda n: reduce(lambda x, _: x+[x[-1] + x[-2]], range(n-2), [0,1])

print(fib(5))

my_list = [5, 4, 3, 2, 1]
print(reduce(lambda x, y: x + y, my_list))

#%%
def fib_long(n):
    result = [0, 1]
    for i in range(n-2):
        result.append(result[-1] + result[-2])
    return result

print(fib_long(8))