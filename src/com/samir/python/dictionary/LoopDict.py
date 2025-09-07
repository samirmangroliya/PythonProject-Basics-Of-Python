dict2 = {"name": "John", "age": 18, "gender": "male", "city": "Ahmedabad", "country": "India", "state": "Gujarat"}

for key in dict2: #key access
    print(key+":"+ str(dict2[key]))
print("\n\nKey Pair For Loop\n")
for key, value in dict2.items(): #key, value
    print(key+":"+ str(value))
