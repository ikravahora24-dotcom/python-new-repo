numbers=[10, 20, 30, 10, 40, 20, 50, 60, 30, 70, 80, 50, 90, 100, 80]
largest=second_largest=float('-inf')
for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num
    elif num >second_largest and num!=largest:
        second_largest = num
print("original numbers:",numbers)
print("Largest:",largest)
print("Second Largest:",second_largest)
