mylist = ["Apple", "Mango", "Grapes", "Orange", "Banana"]
print(mylist)

#in
newList = [x for x in mylist if "g" in x]
print(newList)

#not in
newList2 = [x for x in mylist if "e" not in x]
print(newList2)

newList3 = [x.swapcase() for x in mylist]
print(newList3)

