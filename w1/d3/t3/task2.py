students=[{"name": "Riya", "marks": 88},
    {"name": "Aman", "marks": 95},
    {"name": "Sara", "marks": 72},
    {"name": "John", "marks": 91},
    {"name": "Neha", "marks": 85}]
top_students = students[0]
for student in students:
    if student["marks"] > top_students["marks"]:
        top_students = student
        print("topper name:",top_students["name"])
        print("higest marks:",top_students["marks"])
                        