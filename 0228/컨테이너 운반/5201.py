def container():
    global cnt
    global nums
    global trucks_num
    # 오름차순으로 하나씩 정렬.
    for ti in range(M): #truck 의 적재용량
        for wi in range(nums, N): # 컨테이터의 무게
            if trucks[ti] >= weights[wi]:
                cnt += weights[wi]
                nums +=1
                break
            else: #truck 의 무게가 container 보다 작을 때
                nums +=1
                continue






T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    weights = list(map(int, input().split()))
    trucks = list(map(int,input().split()))
    cnt = 0
    nums = 0
    trucks_num = 0
    weights.sort()
    weights.reverse()
    trucks.sort()
    trucks.reverse()
    # print(weights,trucks)
    container()
    print(f'#{tc} {cnt}')