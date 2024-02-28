from collections import deque

# arr ='1234'
# q = deque(arr)
# print(q)
# q[0] =2
# print()
# q = deque([[1,2]])
direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
for row,col in direction:
    print(type(row))
# q.append([2,3])
# print(q)