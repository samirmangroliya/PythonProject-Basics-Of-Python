dict1 = {"name": "Tata Nexon", "color": "Black","type":"EV Cars", "range":300, "brand":"TATA", "model":"Nexon EV"}
print(dict1)
dict1.pop("color")
print(dict1)
dict1.popitem() #Remove last item from the dictionary.
print(dict1)
del dict1["type"]
print(dict1)
dict1.clear() #clear all element
print(dict1)
del dict1 #delete dictionary completely.
