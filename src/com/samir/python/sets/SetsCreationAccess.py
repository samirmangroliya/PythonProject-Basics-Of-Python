#set is unordered, unchangeable and unindexed. Only add or remove items allowed. Duplicates are not allowed.

mySet = {"Apple", "Banana", "Cherry", "Pineapple", "Grapes", "Orange", "Kiwi"}
print(mySet)
print(mySet)

#True and 1 have same value in set also False and 0
newSet = {"Apple", 1, True, False, 0}
print(newSet)

#length of set
print(len(newSet))

print(type(mySet))

#set defines using set constructor
for x in mySet:
    print(x)

#check is element exist
print("banana" in mySet)
print("banana" not in mySet)


