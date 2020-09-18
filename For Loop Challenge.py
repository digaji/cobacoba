# add up all multiples of 3 and 5 from 1 - 100
total1 = 0
for i in range(1, 100):
    if i % 3 == 0 or i % 5 == 0:
        total1 += i
print(total1)