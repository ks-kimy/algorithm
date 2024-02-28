def eleccart(start,cnt,level):
    global result

    if level == N-1:
        cnt += matrix[start][0]
        if result > cnt:
            result = cnt
        else:
            return
        return

    for new_start in range(1,N): #N 4 이면 1,2,3
        if visited[new_start] == 0:
            visited[new_start] = 1
            cnt += matrix[start][new_start]
            eleccart(new_start,cnt,level+1)
            visited[new_start] = 0
            cnt -= matrix[start][new_start]

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    matrix = [list(map(int,input().split())) for _ in range(N)]
    visited = [0 for _ in range(N)]
    result = 1000
    eleccart(0,0,0)
    print(f'#{tc} {result}')