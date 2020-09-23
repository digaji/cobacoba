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

print("Test for branching")