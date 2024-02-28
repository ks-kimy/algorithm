def max_reward(level):
    global temp_max
    if level == N:
        result = int(''.join(arr))
        if temp_max < result:
            temp_max = result
        return
    for i, j in swap_lst:
        arr[i], arr[j] = arr[j],arr[i]
        if [int(''.join(arr)),level] not in path:
            path.append([int(''.join(arr)),level]) #level 과 그때의 수를 저장한다. 그러면 가지치기를 할 수 있다.
            #만약 다른 스타트 지점으로 출발했을 때 level 이 9가 됐을 때 같은 수가 나왔다면 더이상 진행 할 필요가 없어진다.
            max_reward(level+1)
        arr[i], arr[j] = arr[j],arr[i] #다시 제자리로 돌려준다.

T = int(input())
for tc in range(1, T+1):
    arr, N = input().split()
    length = [i for i in range(len(arr))]
    temp_max = 0
    swap_lst= []
    path = []
    for i in range(len(length)):
        for j in range(i+1,len(length)):
            swap_lst.append([i,j])
# 위의 for 문은 순서를 바꾸는 조합을 나타낸 것이다.
    N = int(N)
    arr = list(arr)
    max_reward(0)
    print(f'#{tc} {temp_max}')

