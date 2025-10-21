def functionTest():
    x = 45
    print(x)

functionTest()

#function inside function

def test():
    str = "function inside function called..."

    def test2():
        print(str)
    test2()

test()



#global variable
day = "Monday"

def dayFunction():
    print(day)

dayFunction()
print(day)


#global variable score and local scope
x = 800

def testLocal():
    x = 900
    print(x)
testLocal()
print(x)

#global keyword
x = 1200
def testGlobal():
    global x
    x = 1500
testGlobal()
print(x)

#nonlocal keyword function
def nonLocalCheck():
    x = "Local"

    def check():
       nonlocal x
       x = "non local"

    check()
    return x

print(nonLocalCheck())



