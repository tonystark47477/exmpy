file = open("source.txt", "r")

lines = []

for line in file:
    lines.append(line.strip())

file.close()

print("Lines stored in list:")
print(lines)


