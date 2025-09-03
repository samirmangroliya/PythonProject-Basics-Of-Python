set1 = {"Apple", 1, False}
tuple1 = ("Apple", 0, True)

print(set1.union(tuple1))

#update
set2 = {"Apple", 1, True}
set3 = {"Banana", 1, False}

set2.update(set3)
print(set2)


#interscation keep only duplicates.
set4 = {"Banana", 1, True}
set5 = {"Banana", 0, False}

set6 = set4.intersection(set5)
print(set6)

#intersaction using & operators
set7 = {"Apple", 1, True}
set8 = {"Banana", 0, False, "Apple"}

set9 = set7 & set8
print(set6)

#intersaction update. it will update set
set10 = {"Apple", True, False}
set11 = {"Apple", 1, 0}
set10.intersection_update(set11)
print(set10)


#difference - will return elements which are not present in first set
set1  = {"Apple", "Cherry", "Banana"}
set2  = {"Samsung", "Google", "Apple"}
print(set1.difference(set2))

#difference using - operators
print(set1-set2)

#diffrence update
set1.difference_update(set2)
print(set1)


#symmetric difference - will keep elements that are not present in both sets
set3  = {"Apple", "Cherry", "Banana"}
set4  = {"Samsung", "Google", "Apple"}
print(set3.symmetric_difference(set4))

#symmetric difference using ^ operator
print(set3^set4)


#symmetric difference update
set3.symmetric_difference_update(set4)
print(set3)

