from collections import deque
arr = [[7, 1], [2, 2], [6, 3], [5, 4], [3, 5]]
q = deque(arr[:2])
arr = deque(arr)
num = arr[0][0]//2
print(arr)
print(num)