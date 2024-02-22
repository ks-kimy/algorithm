# Magnetic
# 1은 N극 -> 아래로, 2는 S극 -> 위로.
def magnetic(matrix):
    global N
    for col in range(N):
        for row in range(N):
            if matrix[row][col] == 1 or matrix[row][col] == 2:
                empty_lst[col].append(matrix[row][col])
    return empty_lst

def sum_mag(lst):
    global cnt
    for temp in lst:
        length = len(temp)
        for i in range(length-1):
            if temp[i] == 1:
                if temp[i+1] ==2:
                    cnt+=1
    return cnt



T = 10
for tc in range(1,11):
    empty_lst= [[] for _ in range(100)]
    cnt = 0
    N = int(input())
    matrix = [list(map(int,input().split())) for _ in range(N)]
    result = magnetic(matrix)
    final = sum_mag(result)
    print(f'#{tc} {final}')