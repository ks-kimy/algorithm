def gravity(N, heights):
    result_num = 0
    for i in range(N):
        sum_number = 0
        for j in range(i+1,N):
            if heights[i] > heights[j]:
                sum_number += 1
        if sum_number > result_num:
            result_num = sum_number
    return result_num

T = int(input())
for t in range(T):
    N = int(input())
    heights = list(map(int, input().split()))

    result = gravity(N,heights)

    print(f'#{T} {result}')

