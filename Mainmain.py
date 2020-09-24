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
