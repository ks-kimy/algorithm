#숫자 배열 회전
def rotation(matrix):
    temp_matrix = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            temp_matrix[i][j] = matrix[N-1-j][i]

    return temp_matrix

T = int(input())
for tc in range(T):
    print(f'#{tc+1}',end='\n')
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    result1 = rotation(matrix)
    result2 = rotation(result1)
    result3 = rotation(result2)
    result = result1 + result2 + result3
    for i in range(N):
        test = ''.join(map(str, result1[i]))
        test2 = ''.join(map(str, result2[i]))
        test3 = ''.join(map(str, result3[i]))
        # print(*result1[i], ' ', sep='', end='')  # 90도 회전한 행렬의 행을 출력합니다.
        # print(*result2[i], ' ', sep='', end='')  # 180도 회전한 행렬의 행을 출력합니다.
        # print(*result3[i], sep='', end='')  # 270도 회전한 행렬의 행을 출력합니다.
        # print()  # 다음 행을 출력하기 전에 줄바꿈을 합니다.
        print(test, test2, test3,end='\n')