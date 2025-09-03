mySet = {"Apple", "Banana", "Cherry", "Pineapple", "Strawberry"}
print(mySet)

#add item
mySet.add("Grapes")
print(mySet)

#add other tuple or collection
newSet = {"Orange", "Custard Apples"}
mySet.update(newSet)
print(mySet)

#adding list in set
myList = ["Kiwi", "Guava"]
mySet.update(myList)
print(mySet)


#Remove element
mySet.remove("Cherry")
print(mySet)

#remove item even item is not exist
mySet.discard("Cherry")

#pop not sure which item will be removed.
x= mySet.pop()
print("item removed is:", x)
print(mySet)

#clear all items
mySet.clear()
print(mySet)

#del set completely
del mySet

