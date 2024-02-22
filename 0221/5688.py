#세제곱근을 찾아라
def triple(N):
    i = 1
    while True:
        if N == i ** 3:
            return i
        elif N != i ** 3:
            i += 1
        if i ** 3 > N:
            return -1
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    result = triple(N)
    print(f'#{tc} {result}')
