newTuple = (1,2,3,4,5,6)
print(newTuple)

myList = list(newTuple) #convert to list

myList[0] = 0 #change 0 index of list
myList.append(7) # add new element
myList.remove(6) #remove element 6

tuple1 = tuple(myList) #convert back to tuple
print(tuple1)


#add tuple to new tuple
x = ("a", "b", "c", "d")
y = ("e", "f", "g", "h")
x +=y
print(x)


newTuple = (1,2,3,4,5,6)
del newTuple
#print(newTuple) #this will give error because tuple is already deleted

