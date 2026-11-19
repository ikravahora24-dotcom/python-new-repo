def create_frozenset(my_list):
    return frozenset(my_list)
numbers = [10,20,30,10,40,20]
result=create_frozenset(numbers)
print("original list:",numbers)
print("frozenset:",result)
print("type:",type(result))
