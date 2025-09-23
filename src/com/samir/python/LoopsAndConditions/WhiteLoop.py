i = 1
while i <= 10:
    print(i)
    i = i + 1

#break
print("Break the while loop")
j = 2
while j < 9:
    if j>6:
        break
    print(j)
    j = j+1

#continue
print("continue the while loop")
k = 0
while k < 5:
    k = k + 1
    if k == 4:
        continue
    print(k)


#while with else
print("else the while loop")
l = 1
while l <= 5:
    print(l)
    l = l + 1
else:
    print("l is more than 5")




