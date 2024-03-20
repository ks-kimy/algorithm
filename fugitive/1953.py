import sys
from collections import deque

sys.stdin = open("input.txt", "r")

def bfs(R,C):
    q.append((R,C))

    while q:
        row , col= q.popleft()
        way = tunel[row][col]
        for drow, dcol in ways[way]:
            nrow = row + drow
            ncol = col + dcol
            if 0<= nrow <N and 0<= ncol <M and tunel[nrow][ncol]>0 and visited[nrow][ncol] == 0:
                if [-drow, -dcol] in ways[tunel[nrow][ncol]]:
                    q.append((nrow,ncol))
                    visited[nrow][ncol] = visited[row][col]+1


T = int(input())

for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    tunel = [list(map(int,input().split())) for _ in range(N)]
    visited = [[0]* M for _ in range(N)]
    visited[R][C] = 1
    q = deque([])
    ways = {
        1 : [[1,0],[-1,0],[0,1],[0,-1]],
        2 : [[1,0],[-1,0]],
        3 : [[0,1],[0,-1]],
        4 : [[-1,0], [0,1]],
        5 : [[1,0], [0,1]],
        6 : [[1,0],[0,-1]],
        7 : [[-1,0],[0,-1]],
    }
    bfs(R,C)
    cnt =0
    for row in range(N):
        for col in range(M):
            if 0< visited[row][col] <= L:
               cnt +=1 
    print(f'#{tc}',end=' ')    
    print(cnt)
    # print(visited)