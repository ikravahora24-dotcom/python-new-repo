matrix=[[1,2,3],
        [4,5,6],
        [7,8,9]]
transpose = [[row[i] for row in matrix ]for i in range(3)]
print("original matrix:")
for row in matrix:
    print(row)
print("transpose matrix:")
for row in transpose:
    print(row)
