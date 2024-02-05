#색칠하기

# print(A)

def color(color_info):
    A = [[0] * 10 for _ in range(10)]
    r1 = color_info[0]
    c1 = color_info[1]
    r2 = color_info[2]
    c2 = color_info[3]
    color = color_info[4]
    for i in range(r1, r2+1):
        for j in range(c1, c2+1):
            A[i][j] += color
    return A

def count_three(matrix):
    cnt = 0
    for i in range(10):
        for j in range(10):
            if matrix[i][j] == 3:
                cnt += 1
    return cnt

T = int(input())
for t in range(T):
    N = int(input())
    A = [[0] * 10 for _ in range(10)]
    for _ in range(N):
        color_info = list(map(int, input().split()))
        matrix = color(color_info)
        for i in range(10):
            for j in range(10):
                A[i][j] += matrix[i][j]
    result = count_three(A)
    print(f'#{t+1} {result}')