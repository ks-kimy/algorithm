#부분집합의 합
T = int(input())
A = list(range(1, 13))
def make_subset():
    n = len(A)
    result = [[] for _ in range(n+1)]
    for i in range(1 << n): #모든 부분집합들의 갯수
        sum_val = cnt_val = 0
        for j in range(n):
            if i & (1 << j):
                sum_val += A[j]
                cnt_val += 1
        result[cnt_val].append(sum_val)
    return result

for t in range(T):
    N, K = map(int, input().split())
    subset = make_subset()
    print(f'#{t+1} {subset[N].count(K)}')
    print(subset)
