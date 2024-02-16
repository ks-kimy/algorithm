# 미로

import time
import math
def maze(size, matrix):
    di = [1,-1,0,0]
    dj = [0,0,1,-1]
    result = 0
    visited = [[0]* size for _ in range(size)]
    stack = []
    for i in range(size):
        for j in range(size):
            if matrix[i][j] == 2:
                row = i
                col = j
                stack.append((row,col))
                break

        # 출발지점 찾고 row 와 col 에 각각 행 열 저장.
    while stack: # 값이 3일 때까지 while 문 동작.
        i, j = stack.pop()
        visited[i][j] =1
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0<=ni<size and 0<=nj <size and not visited[ni][nj]:
                if matrix[ni][nj] == 0:
                    stack.append((ni,nj))
                    # print(stack)
                if matrix[ni][nj] == 3:
                    result = 1
                    stack.clear()
                    break
    return result




T = int(input())

for tc in range(1, T+1):
    size = int(input())
    # print(size)
    matrix = [list(map(int, input())) for _ in range(size)]
    # print(matrix)
    result = maze(size, matrix)
    print(f'#{tc} {result}')
