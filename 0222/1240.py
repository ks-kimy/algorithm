#단순 2진 암호코드
def secret_find(arr):
    global M # arr의 길이.
    end = M-56
    for i in range(end):
        secret = []
        temp = arr[i:i+56]
        for j in range(8):
            part = temp[j*7:(j+1)*7]
            if part in secret_num:
                secret.append(secret_num[part])
            else:
                break
        if len(secret) == 8:
            return secret
    # if
def secret_sum(lst):
    sum_number = 0
    for i in range(0,8,2):
        sum_number += lst[i]*3
    for i in range(1,8,2):
        sum_number += lst[i]
    if sum_number % 10 == 0:
        return sum(lst)
    else:
        return 0

secret_num = {
    '0001101' : 0,
    '0011001' : 1,
    '0010011' : 2,
    '0111101': 3,
    '0100011': 4,
    '0110001': 5,
    '0101111': 6,
    '0111011': 7,
    '0110111': 8,
    '0001011': 9
}

T =int(input())
for tc in range(1, T+1):
    N,M = map(int,input().split())
    matrix = [input() for _ in range(N)]
    # print(matrix)
    for row in range(N):
        if '1' in matrix[row]:
            start_row = row
            break
    result = secret_find(matrix[start_row])
    final = secret_sum(result)
    print(f'#{tc} {final}')
    # print(result)
