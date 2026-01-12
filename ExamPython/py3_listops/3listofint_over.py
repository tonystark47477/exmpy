store = input("Enter numbers: ").split(",")
list = []
for n in store:
    if int(n) > 100:
        list.append("Over")
    else:
        list.append(int(n))
print("Modified list: ",list)