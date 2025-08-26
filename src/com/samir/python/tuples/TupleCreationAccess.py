newTuple = (1,2,3,4,5,6,6,6,6)
print(newTuple)

print(type(newTuple)) #type of tuple
print(newTuple[1]) #access element by index

tuple1 = ("1", "Apple", 2, 'Apple') #any type of element
print(list(tuple1)) # convert tuple to list

mylist2 = [1,2,3,4,5,6,6,6,6]
print(tuple(mylist2)) #convert list to tuple

tuple3  = ("Apple") #it will treat as string
if isinstance(tuple3, tuple):
    print(f"yes {tuple3} is tuple")
else :
    print(f"no {tuple3} is not tuple")


