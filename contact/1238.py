import sys

from collections import deque

def bfs(start):
    q =deque([])
    q.append([start,0])
   

    while q:
        node = q.popleft()
        path.append(node)
        
        for next_node in telephone[node[0]]:
            if not visited[next_node]:
                visited[next_node] = 1
                q.append([next_node,node[1]+1])


sys.stdin = open("input.txt", "r")
T= 10

for tc in range(1,T+1):
    telephone = [[] for _ in range(101)]
    visited = [0 for _ in range(101)]
    N, start = map(int, input().split())
    arr = list(map(int,input().split()))
    path = []
    for i in range(N//2):
        from_ = arr[i*2]
        to_ = arr[i*2 + 1]
        telephone[from_].append(to_)
    print(f'#{tc}',end= ' ')
    visited[start] = 1
    bfs(start)
    path.sort(key=lambda x: (x[1], x[0]))
    print(path[-1][0])
