def myFunction():
    print("my function")

myFunction()


#function with params and return
def add(a, b):
    return a + b

print(add(5, 3))


def cityFunction(city = "Ahmedabad"):
    print("I live in "+city)

cityFunction("Mumbai")
cityFunction(city="Bangalore")
cityFunction()

def nameFunction(fname, lname):
    print(fname+" "+lname)
nameFunction("Hello", "World")
nameFunction("Hello", "Python")


#Arbitrary Arguments, *args no idea how many arguments are there
def functionArbitrary(*args):
    print("Arbitrary function last value::"+args[2])

functionArbitrary("Hello", "World", "Python")

#keyword arguments, order of arguments can change
def functionKeywordArgs(city1, city2, city3):
    print(city1+"->"+city2+"->"+city3)

functionKeywordArgs(city3="Ahmedabad", city2="Bangalore", city1="Mumbai")

#keyword Arbitrary arguments
def functionArbitraryKeywords(**args):
    print("Keyword Arbitrary function last value::"+args["city2"])

functionArbitraryKeywords(city3="Ahmedabad", city2="Bangalore", city1="Mumbai")

#passing list in function

def functionWithList(cities):
    for city in cities:
        print(city)
cities = ["Ahmedabad", "Bangalore", "Mumbai"]
functionWithList(cities)