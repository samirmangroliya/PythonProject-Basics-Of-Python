list1 = ["Apple","Banana", "Cherry", "Dragon fruit"]
list2 = ["Grapes", "Pineapple"]

list3 = list1 + list2
print(list3)

for x in list1:
    list2.append(x)

print(list2)

list4= ["A", "B", "C", "D"]
list5= ["E", "F", "G", "H"]

list4.extend(list5)
print(list4)