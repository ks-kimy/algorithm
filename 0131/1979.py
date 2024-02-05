#어디에 단어가 들어갈 수 있을까
def word_find(matrix,N,M):
    temp_sum1 = 0  # 임시 갯수
    for i in range(N):
        for j in range(N):
            cnt_length = 0  # 하얀색 박스의 연속된 길이
            for k in range(-1, M + 1):  # j-1, j , j+1,j+2,j +3
                nj = j + k
                if 0 <= nj < N:
                    cnt_length += matrix[i][nj]
            if cnt_length == M:
                temp_sum1 += 1
    temp_sum2 = 0  # 임시 갯수
    # for i in range(N):
    #     for j in range(N):
    #         cnt_length = 0  # 하얀색 박스의 연속된 길이
    #         for k in range(-1, M + 1):  # j-1, j , j+1,j+2,j +3
    #             nj = j + k
    #             if 0 <= nj < N:
    #                 cnt_length += matrix[nj][i]
    #         if cnt_length == M:
    #             temp_sum2 += 1
    return temp_sum1 + temp_sum2
# def reverse_matrix(matrix,N):
#     for i in range(N):
#         for j in range(N):
#             matrix[i][j] = matrix[j][i]
#
#     return matrix



T =  int(input())
for t in range(T):
    N, M = map(int,input().split())
    matrix = [list(map(int,input().split())) for _ in range(N)]
    result1 = word_find(matrix,N,M)
    print(result1)