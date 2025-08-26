myList = ["apple", "orange", 'banana', "pineapple"]
print(myList)

#Add element
myList.append("Kiwi")
print(myList)

#insert
myList.insert(0, "WoodApple")
print(myList)

#extend list
newList = ["Water Apple", "Mango", "Strawberry"]
myList.extend(newList)
print(myList)

#add any collection or iterable
myTuple = ("Kiwi", "Grapes")
myList.extend(myTuple)
print(myList)

#Remove
myList.remove("Mango")
print(myList)

#Remove by index
myList.pop(1)
print(myList)

#Remove all elements
myList.clear()
print(myList)