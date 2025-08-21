myList = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print(myList)
print(len(myList))
print(type(myList))

print(myList[2:4]) # index 2..3
print(myList[:4]) # before index 4
print(myList[4:]) # after index 4

#Negative index
print("\n\nNegative Index")
print(myList[-2:])
print(myList[:-3])
print(myList[-4:-1])

#check if element exist in array
if 22 in myList:
    print("22 is in myList")
else :
    print("22 is not in myList")

#change element
myList[0] = "element at index 0"
print(myList)

#change element in range
myList[0:4] = ["apple", "orange", 'banana', "pineapple"]
print(myList)

#insert element
myList.insert(4, "apple2")
print(myList)

#remove element
myList.pop(4)
print(myList)

