import sys
sys.setrecursionlimit(10**8)
def moving_nums(row,col,cnt):

    global result
    if result < cnt:
        result = cnt

    else:
        return
    for drow, dcol in division:
        nrow = row + drow
        ncol = col + dcol
        if 0 <= nrow < N and 0 <= ncol < N and matrix[row][col] +1 == matrix[nrow][ncol]:
            moving_nums(nrow,ncol,cnt+1)
            return
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int,input().split())) for _ in range(N)]
    division = [(1,0), (-1,0),(0,1),(0,-1)]
    start_num = 10000
    temp_max = 0
    for row in range(N):
        for col in range(N): # 출발하는 위치

            result = 0
            cnt = 1
            moving_nums(row,col,cnt)
            if temp_max < result:
                temp_max = result # 갱신되는 부분.
                start_num = matrix[row][col]
            elif temp_max == result and start_num > matrix[row][col]: # 결과 값과 같으면서 시작위치가 더 크다면
                start_num = matrix[row][col] # 더 작은 걸로 교체
    print(f'#{tc} {start_num} {temp_max}')