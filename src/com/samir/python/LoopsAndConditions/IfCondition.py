x = 200
y = 300

if x> y:
    print("x is greater than y")
else:
    print("x is less than y")

#one line condition
print(y) if x>y else print(x)

#elif
if x == y:
    print("x is equal to y")
elif x < y:
    print("x is less than y")
else:
    print("x is greater than y")

z = 500

if x < y and x < z:
    print("x is less than y and z.")

#NOT
if not x > y:
    print("x is not greater than y")

    
