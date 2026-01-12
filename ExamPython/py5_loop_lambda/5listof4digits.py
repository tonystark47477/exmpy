start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))

result = []

for num in range(start, end + 1):
    if num >= 1000 and num <= 9999:
        s = str(num)
        if all(int(d) % 2 == 0 for d in s):
            root = int(num ** 0.5)
            if root * root == num:
                result.append(num)

print("Result:", result)
