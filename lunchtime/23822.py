import sys,math
from collections import deque
sys.stdin = open("input.txt", "r")  

def bfs():
    time = 1
    st1 = 0
    st2 = 0 
    temp1 = deque() # st1 이 꽉 찾을 때의 시각 저장
    temp2 = deque() # st2 이 꽉 찾을 때의 시각 저장
    # st1, st2 는 각각 출구에 3명까지만 있을 수 있게 해주는 기준값.
    while q:
        time += 1
        
        row1,col1,row2,col2 = q.popleft()
        visited[row1][col1] = 1
        visited[row2][col2] = 1
        
        for drow, dcol in direction:
            new_arr = []
            nrow1 = row1 + drow
            ncol1 = col1 + dcol
            nrow2 = row2 + drow
            ncol2 = col2 + dcol
            if 0<=nrow1<N and 0<=col1<N: # 여기서부터 exit1 에 대한
                if not visited[nrow1][ncol1]:
                    visited[nrow1][ncol1] =1
                    if matrix[nrow1][ncol1] == 1:
                        temp1.append(time)
                        new_arr.append([nrow1,ncol1])


            if 0<=nrow2<N and 0<=ncol2<N: # 여기서부터 exit2 에 대한
                if not visited[nrow2][ncol2]:
                    visited[nrow2][ncol2] =1  
                    if matrix[nrow2][ncol2] == 1:
                        temp2.append(time)
                        new_arr.append([nrow2,ncol2])
            add_row1, add_col1, add_row2, add_col2 = 
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    matrix = [list(map(int,input().split())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    q = deque()
    q.append(eixts) # 두개의 exit좌표 [row1,col1,row2,col2]
    direction = [[1,0],[-1,0],[0,1],[0,-1]]
    print(f'{tc}', end=' ')
# q = deque([[[1,2], [2,4]],[[3,4],[5,6]]])
# arr2 = [[3,6],[0,1]]
# q.append(arr2)
# print(q)
# [[[1, 2], [2, 4]], [[3, 4], [5, 6]], [[3, 6], [0, 1]]]