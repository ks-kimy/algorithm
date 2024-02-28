# 미로의 거리
from collections import deque
def search_nums(start,end,matrix):
    # print(start)
    cnt = 0
    start.append(cnt)
    q.append(start)
    # print(q)
    direction = [(1,0),(-1,0),(0,1),(0,-1)]
    while q:
        row, col, cnt = q.popleft()
        for row_d, col_d in direction:
            nrow = row + row_d
            ncol = col + col_d
            if 0<=nrow<N and 0<=ncol<N and matrix[nrow][ncol] == 0:
                q.append((nrow,ncol,cnt+1))
                matrix[nrow][ncol] =1
            elif 0<=nrow<N and 0<=ncol<N and matrix[nrow][ncol] == 3:
                return cnt

    return 0

def find_start(N,matrix):
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 2:
                return [i,j]
def find_end(N,matrix):
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 3:
                return [i,j]



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = deque(list(map(int, input())) for _ in range(N))
    # print(matrix)
    q = deque()
    s_pos = find_start(N,matrix)
    e_pos = find_end(N,matrix)
    result = search_nums(s_pos,e_pos,matrix)
    print(f'#{tc} {result}')