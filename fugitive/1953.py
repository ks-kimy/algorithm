import sys
from collections import deque

sys.stdin = open("input.txt", "r")

def bfs(R,C):
    q.append((R,C,1))

    while q:
        row , col, time = q.popleft()
        way = tunel[row][col]
        for drow, dcol in ways[way]:
            nrow = row + drow
            ncol = col + dcol
            if 0<= nrow <N and 0<= ncol <M and tunel[nrow][ncol]:
                if not visited[nrow][ncol]:
                    visited[nrow][ncol] = time
                    q.append((nrow,ncol,time+1))
        if time == L:
            return


T = int(input())

for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    tunel = [list(map(int,input().split())) for _ in range(N)]
    visited = [[0]* M for _ in range(N)]
    q = deque([])
    ways = {
        1 : [[1,0],[-1,0],[0,1],[0,-1]],
        2 : [[1,0],[-1,0]],
        3 : [[0,1],[0,-1]],
        4 : [[-1,0], [0,1]],
        5 : [[1,0], [0,-1]],
        6 : [[1,0],[0,-1]],
        7 : [[-1,0],[0,-1]],
    }
    bfs(R,C)
    cnt =0
    for row in range(N):
        for col in range(M):
            if visited[row][col]:
               cnt +=1     
    print(cnt)
