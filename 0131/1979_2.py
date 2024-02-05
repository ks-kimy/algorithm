#어디에 단어가 들어갈 수 있을까
def word_find(matrix,N,M):
    temp_matrix =[[0]* (N+1) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 1:
                temp_matrix[i][j+1] = matrix[i][j] +temp_matrix[i][j]
            elif matrix[i][j] == 0:
                temp_matrix[i][j+1] = 0
    return temp_matrix

def reverse_matrix(matrix,N):
    r_matrix = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            r_matrix[i][j] = matrix[j][i]
    return r_matrix
    # 깊은 복사를 통해 matrix 와 r_matrix 를 전혀 다른 객체로 설정
    # 이를 통해 행과 열을 도치 시킨 새로운 r_matrix 를 생성

def count_M(matrix,M):
    cnt = 0
    for lst in matrix:
        for i in lst:
            if i == M:
                cnt += 1
            elif i == M+1:
                cnt -= 1
    return cnt

T =  int(input())
for t in range(T):
    N, M = map(int,input().split())
    matrix = [list(map(int,input().split())) for _ in range(N)]
    cnt_matrix1 = word_find(matrix,N,M)
    result1 = count_M(cnt_matrix1,M)

    matrix2 = reverse_matrix(matrix,N)
    cnt_matrix2 = word_find(matrix2,N,M)
    result2 = count_M(cnt_matrix2,M)
    print(f'#{t+1} {result1+ result2}')
