# Find sum of all negative numbers
given_list3 = [7, 5, 4, 4, 3, 1, -2, -3, -5, -7]
total = 0
i = 0
while i < len(given_list3):
    if given_list3[i] < 0:
        total += given_list3[i]
    i += 1
print(total)