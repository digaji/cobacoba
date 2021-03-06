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

#%%
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 5, 100)
y = np.cos(x)
y2 = np.sin(x)

plt.plot(x, y)
plt.plot(x, y2)
plt.show()

#%%
def average(numbers):
    """
    Args:
        numbers (list): List of numbers

    Returns:
        (int): Average from the list of numbers
    """
    total = sum(numbers)
    total = float(total)
    total = total / len(numbers)
    return total

class Student:
    def __init__(self, name):
        self.name = name
        self.homework = []
        self.quizzes = []
        self.tests = []

    weight = [0.1, 0.3, 0.6]

    def avg_homework(self):
        return average(self.homework)

    def avg_quizzes(self):
        return average(self.quizzes)

    def avg_tests(self):
        return average(self.tests)

    def overall_avg(self):
        return (
            self.avg_homework() * Student.weight[0] +
            self.avg_quizzes() * Student.weight[1] +
            self.avg_tests() * Student.weight[2]
            )

    def is_higher_avg_than(self, another_student):
        return self.overall_avg() > another_student.overall_avg()

eren = Student("Eren")
eren.homework += [90, 97, 75, 92]
eren.quizzes += [88, 40, 94]
eren.tests += [75, 90]

mikasa = Student("Mikasa")
mikasa.homework = [100, 92, 98, 100]
mikasa.quizzes = [82, 83, 91]
mikasa.tests = [89, 97]

print(f"Old avg: {eren.overall_avg()}")
print(f"Old avg: {mikasa.overall_avg()}")

Student.weight = [0.5, 0.3, 0.2]

print(f"New avg: {eren.overall_avg()}")
print(f"New avg: {mikasa.overall_avg()}")

print(f"Is Mikasa's score higher than Eren's?: {mikasa.is_higher_avg_than(eren)}")

#%%
class Animal:  # Abstract Class. You don't create things from this, only inherit from here
    def __init__(self, legs, flavour, weight, lifespan):
        self.legs = legs
        self.flavour = flavour
        self.weight = weight
        self.__lifespan = lifespan

    def makeSound(self):
        return "No Sound"

    def toString(self):
        return "Still Empty"

    def willLive(self, age=None):
        if age == None:
            return f"This animal will usually live for {self.__lifespan} years"
        else:
            return self.willLive() + f" But, this one lives for {age} years"

    def toString(self):
        return (
            f"[legs:{self.legs}, "
            f"flavour:{self.flavour}, "
            f"weight:{self.weight}, "
            f"lifespan:{self.__lifespan}, "
            f"makes sound like:{self.makeSound()}]"
        )

    def getLifespan(self):
        return self.__lifespan

    def setLifespan(self, lifespan):
        if lifespan > 0:
            self.__lifespan = lifespan


class Cat(Animal):
    def __init__(self, flavour, weight):
        super().__init__(4, flavour, weight, 13)

    def makeSound(self):
        return "Meow"


class Fish(Animal):
    def __init__(self, flavor, weight, lifespan):
        super().__init__(0, flavor, weight, lifespan)

    def makeSound(self):
        return "Glug Glug"


my_cat = Cat("Not good", 7)

print(my_cat.makeSound())
print(my_cat.toString())
print(my_cat.willLive())
print(my_cat.willLive(10))

my_fish = Fish("Very good", 9, 1)

print(my_fish.makeSound())
print(my_fish.toString())
print(my_fish.willLive())
print(my_fish.willLive(10))

#%%
class Student:

    def __init__(self):
        self.__sname = ""

    @property
    def sname(self):
        return self.__sname
    
    @sname.setter
    def sname(self, sname):
        if not sname.isnumeric():
            self.__sname = sname

me = Student()
me.sname = "bruh"
print(me.sname)


def check_zero(func):

    def finished(a, b):
        if b == 0:
            return None
        return func(a, b)
    
    return finished

@check_zero
def divide(a, b):
    return a / b

# Other way
def divide2(a, b):
    return a / b
new_divide = check_zero(divide2)

print(divide(7, 2))
print(divide(9, 0))
print(divide(2, 6))
print(divide(5, 9))
print(divide(7, 0))

#%%
import re

data = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin ac erat nec sapien finibus commodo. 
Nullam mattis cursus metus et hendrerit. BK-N130531 Pellentesque non neque magna. Proin auctor arcu augue, 
ac accumsan eros semper sit amet. AB-N175236 In nulla lorem, dapibus nec magna eget, fermentum viverra justo. 
Quisque egestas metus sem, in pretium lectus lobortis suscipit. Sed et porttitor justo, eget condimentum neque. 
Curabitur leo tellus, porta imperdiet nisi finibus, tristique convallis dui."""

pattern = re.compile(r"[A-Z]{2}-N\d{6}")
match = pattern.findall(data)

for i in match:
    print(i)