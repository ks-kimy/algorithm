# 암호생성기
from collections import deque



T = 10

for _ in range(1,T+1):
    tc = int(input())

    arr = deque(map(int, input().split()))
    # print(arr)
    num = arr[0]
    while num:
        for i in range(1,6):
            num = arr.popleft()
            num -= i
            arr.append(num)
            if num <=0:
                num = 0
                arr[7] = num
                break

    print(f'#{tc}', *arr)
    # for i in range(1,6):
    #     num =
