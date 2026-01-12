list1 = input("Enter the colors for list1 separated by commas: ").split(",")
list2 = input("Enter the colors for list2 separated by commas: ").split(",")

print("Colors in list1 not in list2:")
for c in list1:
    if c not in list2:
        print(c)
