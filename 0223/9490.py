#풍선팡
def ballons(N,M):
    max_cnt = 0

    for row in range(N):
        for col in range(M):
            temp = matrix[row][col]
            cnt = matrix[row][col]
            for drow,dcol in direction:
                temp_row = row
                temp_col = col
                for _ in range(temp):
                    temp_row += drow
                    temp_col += dcol
                    if 0<=temp_row<N and 0<=temp_col<M:
                        cnt += matrix[temp_row][temp_col]
            if cnt > max_cnt:
                max_cnt = cnt

    return max_cnt


T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    matrix = [list(map(int,input().split())) for _ in range(N)]
    direction = [(1,0),(-1,0),(0,1),(0,-1)]
    result = ballons(N,M)
    print(f'#{tc} {result}')
