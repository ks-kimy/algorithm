#미로2
from collections import deque


def maze2(matrix):
    direction = [(1,0),(-1,0),(0,1),(0,-1)]
    s_row = 1
    s_col = 1
    # start 지점의 row, col
    q = deque([(s_row, s_col)])
    while q:
        row, col = q.popleft()
        for d_row, d_col in direction:
            nrow = row + d_row
            ncol = col + d_col
            if matrix[nrow][ncol] == 3:
                return 1
            elif matrix[nrow][ncol] == 0:
                matrix[nrow][ncol] = 1
                q.append((nrow,ncol))
    return 0






for tc in range(1,11):
    N = int(input())
    matrix = [list(map(int,input())) for _ in range(100)]
    result = maze2(matrix)
    print(f'#{tc} {result}')
