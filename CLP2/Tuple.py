students = [
 ("Samin", 24, 89),
 ("Foysal", 25, 87),
 ("Mushfik", 28, 85),
 ("Heaven", 23, 95),
 ("Sofiq", 24, 90)
]

SortByGrade = sorted(students, key=lambda x: x[2])

print("Students sorted by grade:")

for student in SortByGrade:
 print(student)
