def timeconverter(sec):
    """some docstring right here"""
    hours = sec // 3600
    minutes = (sec%3600) // 60
    seconds = (sec%3600) % 60
    return hours, minutes, seconds

print(timeconverter(3456))

def my_function(**kid):
    print("His last name is " + kid["lname"])

my_function(fname = "Bagus", lname = "Manuaba")

# def fib(x):
#     if x <= 0:
#         return "Positive integer please"
#     elif x == 1:
#         return 0
#     elif x == 2:
#         return 1
#     else:
#         return fib(x - 1) + fib(x - 2)
        
# print(fib(4))

# def fiblist(x):
#     if x <= 0:
#         return "Positive integer please"
#     elif x == 1:
#         return [0]
#     elif x == 2:
#         return [0, 1]
#     else:
#         n = fiblist(x - 1)
#         n.append(sum(n[: -3: -1]))
#         return n

# print(fiblist(8))

# mylist = [1, 2, 3, 8, 12, 11, 20]
# new = list(filter(lambda x: (x%2 == 0), mylist))
# newmulti = list(map(lambda x: x*2, mylist))
# print(new)
# print(newmulti)

