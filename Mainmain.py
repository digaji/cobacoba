#23 September 2020
#Tuple
a_tuple = (57, "String", 57.0)
print(a_tuple[2])
#Can't .append or .pop with tuple

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

#Make inverse triangle from given height
TRIANGLE_HEIGHT = 5

for i in range(TRIANGLE_HEIGHT):
    print("*" * (i + 1))

for i in range(TRIANGLE_HEIGHT):
    print(" " * (TRIANGLE_HEIGHT - 1 - i) + "*" * (i + 1))

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

def split_and_length(string):
    result1 = []
    for i in string:
        result1.append(i)
    return (result1, len(string))

my_var = "Jason"
chars, length = split_and_length(my_var)
print(chars)
print(length)