import sys,math
from collections import deque
sys.stdin = open("input.txt", "r")  
def find_exit(): # 계단의 위치를 설정. 
    for row in range(N):
        for col in range(N):
            if matrix[row][col] > 1:
                exit.append([row, col])
def find_person(): #사람의 위치 찾기 
    for row in range(N):
        for col in range(N):
            if matrix[row][col]  == 1:
                persons_pos.append([row,col])

def distance(roomposition, stairposition): #거리구하는 함수
    # print(roomposition[0],stairposition[0],roomposition[1],stairposition[1])
    return abs(roomposition[0] - stairposition[0]) + abs(roomposition[1] - stairposition[1])



def stack_count(stair1, stair2): # 계단 1과 계단 2에 스택이 쌓여 있고 먼저 입력된 것부터.
    stair1_len = len(stair1)
    stair2_len = len(stair2)
    stair1.sort(reverse=True)
    stair1.sort(reverse=True)
    if stair1_len != 0:
        t1 = max(stair1) + (math.ceil(stair1_len/3)) * stair_num[0] + stair1_len // 3 +1
    else:
        t1 = 0
    if stair2_len != 0:
        t2 = max(stair2) + (math.ceil(stair2_len/3)) * stair_num[1] + stair2_len // 3 +1
    else:
        t2 = 0
    return max(t1, t2)
     

 
def stair_dfs(num): # stack 에 집어 넣는 과정. num은 person position 의 인덱스 person 은 사람의 좌표 리스트
    if num == persons_num:

        result = stack_count(s1,s2)
        result_arr.append(result)
        # print(s1,s2,result)


        return
    for stair_row,stair_col in exit: # stair 는 exit 의 key 이름.
        
        far = distance(persons_pos[num],[stair_row,stair_col])
        # print(far, persons_pos[num], [stair_row,stair_col])
        if matrix[stair_row][stair_col] == stair_num[0]:
            s1.append(far)
            stair_dfs(num+1)
            s1.pop()
        elif matrix[stair_row][stair_col] == stair_num[1]:
            s2.append(far)
            stair_dfs(num+1)
            s2.pop()

    pass
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    matrix = [list(map(int,input().split())) for _ in range(N)]
    exit = []
    persons_pos = []
    s1 = []
    s2 = []
    find_exit()
    find_person() # 사람들의 위치 인덱스
    persons_num = len(persons_pos)
    # print(matrix)
 
    # print(persons_pos)
    # print(exit)
    stair_num = []
    result_arr=[]
    for row, col in exit:
        stair_num.append(matrix[row][col] )
    print(f'#{tc}')
    stair_dfs(0)
    print(min(result_arr))
    