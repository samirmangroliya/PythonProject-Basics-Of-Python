def replaceChar(func):
    def innerFunc():
        return func().replace("T", "R")
    return innerFunc

@replaceChar
def testReplaceFunc():
    return "Test"

print(testReplaceFunc())


#Arguments in decorator function
def argInDecoratorFunc(func):
    def innerFunc(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return innerFunc

@argInDecoratorFunc
def testArgInDecoratorFunc(name):
    return "Hello "+name

print(testArgInDecoratorFunc("Python"))

#Decorator with Arguments

def decoratorWithArg(n):
    def decorator(func):
        def innerFunc():
            if n == 1:
                x = func().upper()
            else:
                x = func().lower()
            return x
        return innerFunc
    return decorator

@decoratorWithArg(2)
def testDecoratorWithArg():
    return "Test"

print(testDecoratorWithArg())


#multiple decorators
def firstDecoratorFunc(func):
    def innerFunc():
        return func().upper()
    return innerFunc

def secondDecoratorFunc(func):
    def innerFunc():
        return "Hello "+func() + " Have a Great Day!!!"
    return innerFunc

@firstDecoratorFunc
@secondDecoratorFunc
def multipleDecoratorFunc():
    return "Ramesh"

print(multipleDecoratorFunc())




