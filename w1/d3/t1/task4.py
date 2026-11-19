numbers=[10, 20, 30, 10, 40, 20, 50, 60, 30, 70, 80, 50, 90, 100, 80]
unique_numbers =[]
for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)
print("original number:",numbers)
print("list without duplicates:",unique_numbers)