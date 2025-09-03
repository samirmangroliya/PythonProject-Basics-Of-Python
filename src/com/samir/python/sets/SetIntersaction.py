mySet1 = {"Apple", "Banana", "Cherry"}
mySet2 = {"Pomegranate", "Grape", "Apple"}
print(mySet1.intersection(mySet2))

# using & operators
print(mySet1 & mySet2)

#intersection_update will change the original set, it will not return new set
mySet1.intersection_update(mySet2)
print(mySet1)

set1 = {"Apple", 1, False}
set2 = {"Cherry", 0, True, "Apple"}
print(set1.intersection(set2))