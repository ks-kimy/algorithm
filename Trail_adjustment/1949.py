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


T = int(input())
for tc in range(1, T+1):
    N, K = map(int,input().split())
    trails = [list(map(int,input().split())) for _ in range(N)]
    direction = [(1,0),(-1,0),(0,1),(0,-1)]
    start_point =[]
    start_position(trails,N)
    print(f'#{tc} {start_point}')