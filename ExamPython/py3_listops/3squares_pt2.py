nums = input("Enter list of numbers: ").split(",")

squares = []
for n in nums:
    squares.append(int(n) ** 2)

print("Squares:", squares)
