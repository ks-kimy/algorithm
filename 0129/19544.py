#테스트케이스 T를 받는다.
T = int(input())
print(T, type(T))
for t in range(T):
    N = int(input())
    a = list(map(int, input().split()))
    print(N)
    print(a)
    max_val = max(a)
    min_val = min(a)
    print(f'#{t+1} {max_val - min_val}')