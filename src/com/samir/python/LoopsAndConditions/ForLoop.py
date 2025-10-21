fruits = ["apple", "banana", "orange"]

for item in fruits:
    print(item)

for x in [0, 1, 2]:
        pass

for x in range(2, 30, 5): #start from 2 and step up by 5 until 30
  print(x)

  for x in "banana": #string to char
      print(x)

print("For loop with break")
fruits = ["apple", "banana", "orange", "mango", "lemon"]
for x in fruits:
    if x == "orange":
        break
    print(x)

for x in range(4):
    print(x)
else:
   print("For loop finished!")

for index, item in enumerate(fruits):
    print(index, item)
else:
    print("For loop with index finished!")


for index, item in enumerate(fruits):
    print(index, item)
else:
    print("For loop with index finished!")

for index, item in enumerate(fruits):pass