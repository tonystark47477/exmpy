pos = input("Enter integers: ").split(",")
poslist = []
for n in pos:
    if int(n) > 1:
        poslist.append(int(n))
print("Positive numbers: ",poslist)