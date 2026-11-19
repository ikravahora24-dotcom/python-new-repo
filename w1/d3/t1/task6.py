students=[("Riya", 85), ("Aman", 55), ("Sara", 65)]
sorted_students=sorted(students,key=lambda student:student[0],reverse=True)
print("students sorted by marks:")
print(sorted_students)
