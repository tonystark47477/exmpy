def fact(n):
    f = 1
    for i in range(1, n + 1):
        f = f * i
    return f

n = int(input("Enter n: "))
total = 0

for i in range(1, n + 1):
    total = total + fact(i) / fact(i)

print("Sum of series:", total)
