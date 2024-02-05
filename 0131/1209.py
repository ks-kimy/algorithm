#sum 문제

def cross_sum(matrix):
    temp = 0
    for i in range(100):  # 행에 대한 정보
        temp += matrix[i][i]  # 열에 대한 정보
    return temp

def incross_sum(matrix):
    temp = 0
    for i in range(100):  # 행에 대한 정보
        temp += matrix[i][99-i]
    return temp

def horizon_sum(matrix):
    temp = 0
    for i in range(100): # 행에 대한 정보
        temp_sum = 0
        for j in range(100): #열에 대한 정보
            temp_sum += matrix[i][j]
        if temp < temp_sum:
            temp = temp_sum
    return temp

def vertical_sum(matrix):
    temp = 0
    for i in range(100): # 열에 대한 정보
        temp_sum = 0
        for j in range(100): #행에 대한 정보
            temp_sum += matrix[j][i]
        if temp < temp_sum:
            temp = temp_sum
    return temp

T = 10
for t in range(T):
    M = int(input())
    C = [list(map(int, input().split())) for _ in range(100)]
    num1 = incross_sum(C)
    num2 = cross_sum(C)
    num3 = vertical_sum(C)
    num4 = horizon_sum(C)
    # print(num1, num2, num3, num4)
    print(f'{t+1} {max(num1, num2, num3, num4)}')