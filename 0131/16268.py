#풍선팡2
def bumb_sum(matrix):
    max_sum = 0
    di = [0,1,0,-1]
    dj = [1,0,-1,0]
    for i in range(N):
        for j in range(M):
            temp_sum = matrix[i][j]
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < N and 0 <= nj <M:
                    temp_sum += matrix[ni][nj]
            if temp_sum >= max_sum:
                max_sum = temp_sum
    result = max_sum
    return result




T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    result = bumb_sum((matrix))
    # print(N,M)
    # print(matrix)

    print(f'#{t+1} {result}')