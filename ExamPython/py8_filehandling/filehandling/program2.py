file = open("source.txt", "r")
dest = open("destination.txt", "w")

line_no = 1

for line in file:
    if line_no % 2 != 0:
        dest.write(line)
    line_no += 1

file.close()
dest.close()

print("Odd lines copied successfully")
