students = {}

n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter student name: ")
    marks = []

    for j in range(3):
        mark = int(input("Enter mark: "))
        marks.append(mark)

    students[name] = marks

for name, marks in students.items():
    total = sum(marks)
    average = total / 3

    print("Student:", name)
    print("Marks:", marks)
    print("Total:", total)
    print("Average:", average)
