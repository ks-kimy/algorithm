# 1 은 N 극-> 아래로, 2 는 S 극 -> 위로.
from collections import deque
def magnetic_num(arr):
    result = 0
    arr_q = deque(arr)
    temp = 0
    for i in range(len(arr)):
        if temp == 1 and arr_q[0] ==2:
            result += 1
            temp = arr_q.popleft()
        else:
            temp = arr_q.popleft()
    return result





def magnetic():
    cnt = 0
    for col in range(N):
        arr = []
        for row in range(N):
            if matrix[row][col] != 0:
                arr.append(matrix[row][col])
        cnt += magnetic_num(arr)
    return cnt

for tc in range(1,11):
    N = int(input())
    matrix = [list(map(int,input().split())) for _ in range(100)]
    cnt = 0
    result = magnetic()
    print(f'#{tc} {result}')