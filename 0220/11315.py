#오목 판정
def vector(temp_arr,vec): # temp_arr 는 시작 위치, vec 은 방향
    i = 0
    new_arr = temp_arr[:]
    while True :
        # print(arr)
        new_arr[0] += vec[0]
        new_arr[1] += vec[1]
        if new_arr not in arr:
            i +=1
            return i
        else:
            i += 1

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [input() for _ in range(N)]
    # print(matrix)
    arr = []
    for i in range(N):
        for j in range(N):
            if matrix[i][j] =='o':
                arr.append([i,j])
    # print(arr)

    direction = [[1,0],[0,1],[1,1],[1,-1]] # 아래, 오른, 오른대각,왼쪽대각
    result_i = []
    for vec_arr in arr:
        for i in range(4):
            # print(vec_arr,direction[i])

            result = vector(vec_arr, direction[i])
            result_i.append(result)
    if 5 in result_i:
        print(f'#{tc} YES')
    else:
        print(f'#{tc} NO')