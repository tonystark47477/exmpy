list1 = input("Enter numbers: ").split(",")
oddlist = []
for n in list1:
    if int(n) % 2 != 0:
        oddlist.append(int(n))
print("List without even numbers = ",oddlist)