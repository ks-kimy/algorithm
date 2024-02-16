# 회전
from collections import deque

T = int(input())
for tc in range(1,T+1):
    print(f'#{tc}',end=' ')
    N, M = map(int, input().split())
    arr = deque(map(int, input().split()))

    for i in range(M):
        arr.rotate(-1)

    print(arr.popleft())