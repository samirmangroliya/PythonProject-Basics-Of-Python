a = {"apple", "banana", "cherry"}
b = {"grapes", "dragon fruit"}
c = {"User1", "User2", "User3", "User4"}
d  = {"product1", "product2", "product3"}
d1 = {1,2,3,4,5}

#union function returns set while update function didn't return anything
e = a.union(b)
print(e)

# using | operator
f = a | b
print(f)

#join multiple set
g = a.union(b,c,d)
print(g)

#join multiple set using | operator
h = a | b | c | d | d1
print(h)

#join set and tuple
mySet = {1,2,3,4,5}
myTuple = (6,7,8,9,10)
newSet = mySet.union(myTuple)
print(newSet)
