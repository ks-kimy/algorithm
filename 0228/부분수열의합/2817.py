def part_perf():
    global cnt

    for i in range(1<<N):
        result_arr = []
        for k in range(N):
            if i & 0x1:
                result_arr.append(arr[k])
                i >>= 1
            else:
                i >>= 1
        if sum(result_arr) == K:
            cnt+=1


T = int(input())
for tc in range(1, T+1):
    N, K = map(int,input().split())
    arr = list(map(int,input().split()))
    cnt = 0
    part_perf()
    print(f'#{tc} {cnt}')

