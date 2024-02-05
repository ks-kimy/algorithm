T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    a = list(map(int, input().split()))
    min_num = 0
    max_num = 0
    # print(min_num, sum_num, sum_num2,max_num)

    for j in range(M):
        min_num += a[j]
    # print('fdas',min_num)
    for i in range(N-M+1):
        sum_num = 0

        for j in range(i, i+M):
            sum_num += a[j]
            # print(j, end=' ')
        if max_num <= sum_num:
            max_num = sum_num
        # print(max_num)

    for i in range(N-M+1):
        sum_num2 = 0

        for j in range(i, i+M):
            sum_num2 += a[j]
        if min_num >= sum_num2:
            min_num = sum_num2
    # print(min_num)
    print(f'#{t+1} {max_num - min_num}')
    # print(min_num, sum_num, sum_num2,max_num)
