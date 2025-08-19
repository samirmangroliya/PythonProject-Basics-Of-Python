x = str(3)
print(type(x))

#Multiple assign value...
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#multiple value
x="Python"
y = "is"
z ="osm language"

print(x,y,z)

#one value to multiple variable.
x=y=z=3
print(x,y,z)

#unpack collection
fruits = ["Mango","apple", "banana", "cherry"]
w,x,y,z = fruits
print(w,x,y,z)


x = 'awesome'
def myfunc():
  x = 'fantastic'
myfunc()
print('Python is ' + x)
