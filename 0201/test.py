matrix= [list(map(int, input().split())) for i in range(9)]

# for j in range(9):
#     lst2 = list(matrix[k][j] for k in range(9))
#     print(lst2)
#     lst2.sort()
#     print(lst2)

for i in range(9):
    lst1 = matrix[i].sort()
    print(matrix[i])