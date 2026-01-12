students = {
    "Arun": [85, 90, 78],
    "Gowri": [72, 88, 91],
    "Vishnu": [95, 80, 85]
}

for name, marks in students.items():
    total = sum(marks)
    average = sum(marks) / len(marks)

    print("Student:", name)
    print("Marks:", marks)
    print("Total Marks:", total)
    print("Average Marks:", round(average, 2))
    print("*" * 20)
