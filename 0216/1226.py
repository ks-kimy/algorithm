#미로1
def maze1(row,col,matrix):
    # print(row,col)
    visited.append([row,col])
    # print(visited)
    row_d = [1,-1,0,0]
    col_d = [0,0,1,-1]
    # 아래, 위, 오, 왼
    global result
    for k in range(4):
        nrow = row+row_d[k]
        ncol = col+col_d[k]
        if matrix[nrow][ncol]=='3':
            result = 1
        elif matrix[nrow][ncol] == '0'\
                and [nrow, ncol] not in visited:
            maze1(nrow, ncol, matrix)

T = 10
for tc in range(1,T+1):
    N = int(input())
    matrix = [input() for _ in range(16)]
    visited = []
    result = 0
    maze1(1,1,matrix)
    print(f'#{tc} {result}')
    # 1,1 에서 출발