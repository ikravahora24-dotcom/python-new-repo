employees = {
    "Rahul": 45000,
    "Priya": 65000,
    "Amit": 35000,
    "Neha": 80000,
    "Karan": 55000,
    "Riya": 90000
}
sorted_employees = sorted(
    employees.items(),
    key = lambda x:x[1], reverse = True)

print("top three highest paid employees:")
for name,salary in sorted_employees[::3]:
    print(name,":",salary)