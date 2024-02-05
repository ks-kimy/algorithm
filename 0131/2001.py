#파리퇴치 게임
def moving(matrix,N,M):
    pass

def bugs_killer(matrix,N,M):
    max_sum = 0
    for i in range(N):
        for j in range(N):
            temp_sum = 0
            for k in range(M):
                ni = i + k
                for l in range(M):
                    nj = j + l
                    if ni < N and nj < N:
                        temp_sum += matrix[ni][nj]
            if temp_sum > max_sum:
                max_sum = temp_sum
    return max_sum


T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    result = bugs_killer(matrix, N,M)
    print(f'#{t+1} {result}')