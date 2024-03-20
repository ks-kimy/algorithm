import sys
sys.stdin = open("input.txt","r")
def start_position(matrix,N):
    temp = 0 
    for row in range(N):
        for col in range(N):
            if temp < matrix[row][col]:
                temp = matrix[row][col]
                start_point.clear()
                start_point.append([row,col])
            
            elif temp == matrix[row][col]:
                start_point.append([row,col])

def bfs(row,col,length):
    global result
    global K
    global can_dig
    if result <= length:
        result = length
    visited[row][col] = 1 # 처음 방문한 것 방문 처리
    for drow, dcol in direction:
        recent_height = trails[row][col]
        nrow = drow + row
        ncol = dcol + col
        if 0 <= nrow < N and 0 <= ncol < N and visited[nrow][ncol] == 0:
            if trails[nrow][ncol] < recent_height:
                bfs(nrow,ncol,length+1)
                visited[nrow][ncol] = 0
            elif trails[nrow][ncol] > recent_height and can_dig:
                for i in range(K,-1,-1):
                    if trails[nrow][ncol] - i < recent_height:
                        trails[nrow][ncol] -= i
                        can_dig -=1
                        
                        bfs(nrow,ncol,length+1)
                        can_dig += 1
                        trails[nrow][ncol] += i
                        visited[nrow][ncol] == 0
                    if trails[nrow][ncol] - i == recent_height:
                        break
            elif trails[nrow][ncol] == recent_height and can_dig:
                for i in range(1,K+1):
                    trails[nrow][ncol] -= i 
                    can_dig -= 1
                    
                    bfs(nrow,ncol,length+1)
                    can_dig += 1
                    trails[nrow][ncol] += i
                    visited[nrow][ncol] = 0
    visited[row][col] = 0 # 위의 모든 과정들이 끝나면 방문 처리를 풀어준다. 


T = int(input())
for tc in range(1, T+1):
    N, K = map(int,input().split())
    can_dig = 1
    trails = [list(map(int,input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    direction = [(1,0),(-1,0),(0,1),(0,-1)]
    start_point =[]
    result = 0
    start_position(trails,N)
    # print(f'#{tc} {start_point}')
    for row, col in start_point:
        bfs(row,col,1)
    print(f'#{tc} {result}')