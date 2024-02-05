#회문
def reverse_words(arr):
    length = len(arr)
    for i in range(length//2):
        arr[i] ,arr[length-1-i] = arr[length-1-i], arr[i]
    return arr

def print_words(matrix):
     for i in range(N):
        for j in range(N-M+1):
            temp_arr = matrix[i][j:j+M]
            arr_org = ''.join(temp_arr)
            temp_arr2 = reverse_words(temp_arr)
            arr_rev = ''.join(temp_arr2)
            if arr_org == arr_rev:
                return arr_org
def reverse_matrix(matrix):
    temp_matrix = [['']*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            temp_matrix[i][j] = matrix[j][i]

    return temp_matrix

T = int(input())
for tc in range(T):
    N,M = map(int, input().split())
    matrix = [list(input()) for _ in range(N)]
    rev_matrix = reverse_matrix(matrix)
    result1 = print_words(matrix)
    result2 = print_words(rev_matrix)
    if result1:
        result = result1
    elif result2:
        result = result2

    print(f'#{tc+1} {result}')



