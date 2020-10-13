# 1. Func to round up a number to specified digits
# def roundup(x, y):
#     return round(x, y)

# print(roundup(123.01247, 4))

# 2. Convert RGB to HSV
# def convert(r, g, b):
#     clist = [r, g, b]
#     R = r / 255
#     G = g / 255
#     B = b / 255
#     clist = [R, G, B]
#     cmax = sorted(clist)[2]
#     cmin = sorted(clist)[0]
#     if (cmax - cmin == 0):
#         h = 0
#     elif cmax == R:
#         h = (60 * ((G - B) / cmax - cmin) + 360) % 360
#     elif cmax == G:
#         h = (60 * ((B - R) / cmax - cmin) + 120) % 360
#     elif cmax == B:
#         h = (60 * ((R - G) / cmax - cmin) + 240) % 360
#     if cmax == 0:
#         s = 0
#     else:
#         s = (((cmax - cmin)) / cmax) * 100
#     v = cmax * 100
#     print("RGB > {},{},{}".format(r, g, b))
#     print("HSV > ", (h, s, v))

# convert(0, 215, 0)

# 3. Find perfect squares between 2 given numbers
# def squares(x, y):
#     square = []
#     for i in range(x, y + 1):
#         sqrt = i ** 0.5
#         modulus = sqrt % 1
#         if modulus == 0:
#             square.append(i)
#     return square

# print(squares(1, 30))

# 4. Given string, display only characters which are present at an even index
# string = "Mr. Miyabi"
# alist = []
# for i in string:
#     if string.index(i) % 2 == 0:
#         alist.append(i)
# print(alist)

# 5. Given list of numbers, return True if first and last number of list same
# Yes = [10, 20, 30, 40, 10]
# No = [10, 20, 30, 40, 50]

# def isitsame(x):
#     print("Given list is ", x)
#     if x[0] == x[-1]:
#         print("result is True")
#     else:
#         print("result is False")

# isitsame(Yes)
# isitsame(No)

# 6. Given list of numbers, iterate and print only those numbers which are divisible of 5
# woah = [10, 20, 33, 46, 55]

# def ambil5(x):
#     print("Given list is ", x)
#     print("Divisible of 5 in a list")
#     for i in x:
#         if i % 5 == 0:
#             print(i)

# ambil5(woah)

# 7. Reverse a given number and return True if it is the same as the original number
# origin1 = 121
# origin2 = 125

# def checkreverse(x):
#     y = str(x)[::-1]
#     y = int(y)
#     if x == y:
#         print("The original and reverse number is the same")
#     else:
#         print("The original and reverse number is not same")

# checkreverse(origin1)
# checkreverse(origin2)

# 8. Given a 2 list of numbers, create a new list such that new list should contain odd numbers from 1st list 
#    and even numbers from 2nd list
# listUno = [10, 20, 23, 11, 17]
# listDos = [13, 43, 24, 36, 12]

# def ngefilter(x, y):
#     newlist = []
#     for i in x:
#         if i % 2 != 0:
#             newlist.append(i)
#     for i in y:
#         if i % 2 == 0:
#             newlist.append(i)
#     print(newlist)

# ngefilter(listUno, listDos)

# 9. Calculate income tax for the given income by adhering to the below rules
# taxIncome = 45000

# def taxpayable(income):
#     if income >= 20000:
#         tax = (10000*10/100) + ((income - 20000)*20/100)
#     else:
#         tax = ((income - 10000)*10/100)
#     print(tax)

# taxpayable(taxIncome)

# 10. Print multiplication table from 1 to 10
for i in range(1, 11):
    print(i, str(list(map(lambda x: i * x, range(2, 11)))).replace(',', '')[1:-1])