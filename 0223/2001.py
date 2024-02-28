#파리 퇴치
def kill_mosq(N,M):
    max_sum = 0
    for row in range(N-M+1):
        for col in range(N-M+1):
            temp = 0
            for i in range(M):
                temp += sum(matrix[row+i][col:col+M])
            if max_sum < temp:
                max_sum = temp
            # print(max_sum
            #       )
    return max_sum

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    matrix = [list(map(int,input().split())) for _ in range(N)]
    result = kill_mosq(N,M)
    print(f'#{tc} {result}')