dict1 = {
    "name" : "Samir",
    "age" : 22,
    "gender" : "male"
}

print(dict1)
dict1["city"] = "Vadodara"
print(dict1)
print(len(dict1))
print(type(dict1))

#access item
print(dict1.get("name"))
print(dict1["age"])

#all keys
print(dict1.keys())

#all values
print(dict1.values())

#items return in dictionary
print(dict1.items())

#add item in dictionary
dict1["email"] = "test@gmail.com"
print(dict1)

#check key in dict
if "name" in dict1:
    print("Yes name key is in dict1")

