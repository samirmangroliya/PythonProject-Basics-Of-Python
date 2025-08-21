print("\nHello World\n")
print("It's single quote 'yes like this'")

x = "Hello World"
print(x)

#multiline string
x = """
multi
line
string"""
print(x)

#strings are array
x = "Hello World"
print(x[0]) #0 th index

#string for loop
for x in "Apple":
    print(x)

#string len
x = "Apple"
print("length of Apple:", len(x))

#check string is available inside other string
strText = "Hello World"
if "Hello" in strText:
    print("Yeah, Hello is present in Hello World")

#check if not
strText = "Hello World"
if "hello" not in strText:
    print("hello is NOT present in Hello World")





