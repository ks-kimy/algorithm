import sys
from collections import deque

sys.stdin = open("input.txt", "r")

def bfs(N,M):
    q = deque([])
    q.append([N,0])
    while q:
        number = q.popleft()
        num = number[0]
        cnt = number[1]
        if num == M:
            return cnt
        
        if 0 < num*2 <= 1000000 and num*2 not in visited:
            visited.add(num*2)
            q.append([num*2,cnt+1])
       
        if 0 < num-10 <= 1000000 and num-10 not in visited:
            visited.add(num-10)
            q.append([num-10,cnt+1])
       
        if 0 < num-1 <= 1000000 and num-1 not in visited:
            visited.add(num-1)
            q.append([num-1,cnt+1])
       
        if 0 < num+1 <= 1000000 and num+1 not in visited:
            visited.add(num+1)
            q.append([num+1,cnt+1])



T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    visited = set()
    result = bfs(N,M)
    print(f'#{tc} {result}')
