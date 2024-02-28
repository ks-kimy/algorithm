def recursion_max(row,col,cnt):
    global result
    if result < cnt:
        return


    if row < N-1:
        recursion_max(row+1,col,cnt + matrix[row+1][col]) # 아래로 먼저 돈다.
    if col < N-1:
        recursion_max(row,col+1,cnt + matrix[row][col+1]) # 위의 재귀 과정이 끝나면 오른쪽으로.
    if row == N - 1 and col == N - 1:
        if result > cnt:
            result = cnt
        else:
            return
        return

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int,input().split())) for _ in range(N)]
    cnt = matrix[0][0]
    result = 100
    answer = 0
    recursion_max(0,0,cnt)
    print(f'#{tc}', end=" ")
    print(result)
