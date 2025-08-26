newTuple = ("Apple", "Banana", "Cherry")
print(newTuple)

a,b,c = newTuple
print(a)
print(b)
print(c)

#Asterisk, assigned value as list if variables are less than elements
newTuple2 = ("Apple", "Banana", "Cherry", "Pineapple", "Grapes", "Orange", "Kiwi")
a,b, *c, d = newTuple2
print(a)
print(b)
print(c)
print(d)

