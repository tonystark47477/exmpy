students = {
    "Arun":78,
    "Beena":85,
    "Charan": 72,
    "Divya": 90
}
print("Original dictionary ",students)

asc_byname = dict(sorted(students.items()))
print("Sorted by name: ",asc_byname)
desc_byname = dict(sorted(students.items(),reverse=True))
print("Descending order: ",desc_byname)