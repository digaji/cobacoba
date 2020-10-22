#%%
age = eval(input("Type in your age: "))
sex = input("Type in your sex [M/F]: ")
marriage = input("Type in your marital status [Y/N]: ")

#%%
def determineplace(x, y, z):
    if y == "F":
        print("Urban")
    elif y == "M":
        if 20 <= age <= 40:
            print("Anywhere")
        elif 40 < age <= 60:
            print("Urban")
        else:
            print("ERROR")
    else:
        print("Sex is wrong")  # Astaga


determineplace(age, sex, marriage)

# Level 1
#%%
# 1. Print all elements of a list using for loop.
for i in [1, 2, 3, 4]:
    print(i)
#%%
# 2. Take inputs from user to make a list.
#    Again take one input from user and search it in the list and delete that element,
#    if found. Iterate over list using for loop.
n = list(input("Type some numbers here: ").split())
n1 = input("Type a number you want to delete: ")

if n1 in n:
    n.remove(n1)
for i in n:
    print(i)
#%%
# 4. You are given with a list of integer elements. Make a new list which will store square of elements of previous list.
n = [1, 2, 3, 4]
b = []
for i in n:
    b.append(i ** 2)
print(b)

#%%
# 5. Using range(1,101), make two list, one containing all even numbers and other containing all odd numbers.
odd = []
even = []

for i in range(1, 101):
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
print(odd)
print(even)

#%%
# 6. From the two list obtained in previous question, make new lists,
#    containing only numbers which are divisible by 4, 6, 8, 10, 3, 5, 7 and 9 in separate lists.
odd = []
even = []
for i in range(1, 101):
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

four = []
six = []
eight = []
ten = []
three = []
five = []
seven = []
nine = []

for i in even:
    if i % 4 == 0:
        four.append(i)
    if i % 6 == 0:
        six.append(i)
    if i % 8 == 0:
        eight.append(i)
    if i % 10 == 0:
        ten.append(i)

for i in odd:
    if i % 3 == 0:
        three.append(i)
    if i % 5 == 0:
        five.append(i)
    if i % 7 == 0:
        seven.append(i)
    if i % 9 == 0:
        nine.append(i)
print(four, six, eight, ten, three, five, seven, nine)

#%%
# 7. From a list containing ints, strings and floats, make three lists to store them separately.
n = [2, 4, "Yo", "Yey", "Bro", 2.0, 4.0, 3.0, 1.0]
ints = []
strings = []
floats = []

for i in n:
    if type(i) == int:
        ints.append(i)
    elif type(i) == str:
        strings.append(i)
    else:
        floats.append(i)

print(ints, strings, floats)

#%%
# Level 2
# 1. Using range(1,101), make a list containing only prime numbers.
primes = []
for num in range(2, 101):
    prime = True
    for i in range(2, num):
        if (
            num % i == 0
        ):  # Checks if num can be divided by any number below it other than 1
            prime = False
    if prime:
        primes.append(num)

print(primes)

#%%
# 2.
# Initialize a 2D list of 3*3 matrix. E.g.
# 1	 2	3
# 2	 4	5
# 3	 5	6
# Check if the matrix is symmetric or not.
a = [[1, 2, 3], [2, 4, 5], [3, 5, 6]]
sym = True
for i in range(0, 3):
    for j in range(0, 3):
        if a[i][j] != a[j][i]:
            sym = False
print(sym)

#%%
# 3. Sort without using sort()
a = [2, 3, 1, 45, 15]
print(a)
for i in range(0, len(a)):
    for e in range(i + 1, len(a)):
        if a[i] > a[e]:
            a[i], a[e] = a[e], a[i]

print(a)

#######################################################
#%%
# 1. Func to round up a number to specified digits
def roundup(x, y):
    return round(x, y)


print(roundup(123.01247, 4))

#%%
# 2. Convert RGB to HSV
def convert(r, g, b):
    clist = [r, g, b]
    R = r / 255
    G = g / 255
    B = b / 255
    clist = [R, G, B]
    cmax = sorted(clist)[2]
    cmin = sorted(clist)[0]
    if cmax - cmin == 0:
        h = 0
    elif cmax == R:
        h = (60 * ((G - B) / cmax - cmin) + 360) % 360
    elif cmax == G:
        h = (60 * ((B - R) / cmax - cmin) + 120) % 360
    elif cmax == B:
        h = (60 * ((R - G) / cmax - cmin) + 240) % 360
    if cmax == 0:
        s = 0
    else:
        s = (((cmax - cmin)) / cmax) * 100
    v = cmax * 100
    print("RGB > {},{},{}".format(r, g, b))
    print("HSV > ", (h, s, v)) # type: ignore


convert(0, 215, 0)

#%%
# 3. Find perfect squares between 2 given numbers
def squares(x, y):
    square = []
    for i in range(x, y + 1):
        sqrt = i ** 0.5
        modulus = sqrt % 1
        if modulus == 0:
            square.append(i)
    return square


print(squares(1, 30))

#%%
# 4. Given string, display only characters which are present at an even index
string = "Mr. Miyabi"
alist = []
for i in string:
    if string.index(i) % 2 == 0:
        alist.append(i)
print(alist)

#%%
# 5. Given list of numbers, return True if first and last number of list same
Yes = [10, 20, 30, 40, 10]
No = [10, 20, 30, 40, 50]


def isitsame(x):
    print("Given list is ", x)
    if x[0] == x[-1]:
        print("result is True")
    else:
        print("result is False")


isitsame(Yes)
isitsame(No)

#%%
# 6. Given list of numbers, iterate and print only those numbers which are divisible of 5
woah = [10, 20, 33, 46, 55]


def ambil5(x):
    print("Given list is ", x)
    print("Divisible of 5 in a list")
    for i in x:
        if i % 5 == 0:
            print(i)


ambil5(woah)
#%%
# 7. Reverse a given number and return True if it is the same as the original number
origin1 = 121
origin2 = 125


def checkreverse(x):
    y = str(x)[::-1]
    y = int(y)
    if x == y:
        print("The original and reverse number is the same")
    else:
        print("The original and reverse number is not same")


checkreverse(origin1)
checkreverse(origin2)

#%%
# 8. Given a 2 list of numbers, create a new list such that new list should contain odd numbers from 1st list
#   and even numbers from 2nd list
listUno = [10, 20, 23, 11, 17]
listDos = [13, 43, 24, 36, 12]


def ngefilter(x, y):
    newlist = []
    for i in x:
        if i % 2 != 0:
            newlist.append(i)
    for i in y:
        if i % 2 == 0:
            newlist.append(i)
    print(newlist)


ngefilter(listUno, listDos)

#%%
# 9. Calculate income tax for the given income by adhering to the below rules
taxIncome = 45000


def taxpayable(income):
    if income >= 20000:
        tax = (10000 * 10 / 100) + ((income - 20000) * 20 / 100)
    else:
        tax = (income - 10000) * 10 / 100
    print(tax)


taxpayable(taxIncome)

#%%
# 10. Print multiplication table from 1 to 10
for i in range(1, 11):
    print(i, str(list(map(lambda x: i * x, range(2, 11)))).replace(",", "")[1:-1])
