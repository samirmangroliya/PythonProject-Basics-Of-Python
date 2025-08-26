mylist = ["Apple", "Mango", "Grapes", "Orange"]
print(mylist)

for x in mylist:
    print(x)

for x in range(len(mylist)):
    print(f"element at index {x} is: {mylist[x]}")

#while loop
i = 0
while i< len(mylist):
    print(f"While loop: {mylist[i]}")
    i += 1


