#노드의거리
from collections import deque
def nodes(V,E,S,G,q):
    visited = [0] * (V+1) # 방문한 것.
    cnt = 0
    # q는 n번째 노드에 연결된 노드들을 나타낸 것.
    set_q = deque([[S,cnt]]) #출발하는 지점의 노드 넘버.
    while set_q:
        start = set_q.popleft() # start 포인트와 cnt 가 같이 나옴.
        visited[start[0]] =1
        for i in q[start[0]]: # 위치한 노드의 연결된 노드들 i
            if visited[i]: # 만약 방문한 곳이라면
                continue
            else:
                set_q.append([i,start[1]+1])

        if start[0] == G:
            return start[1]
    return 0

T = int(input())
for tc in range(1,T+1):
    V, E = map(int, input().split())
    q = [[] for _ in range(V+1)]
    arr = []
    for _ in range(E):
        arr.append(list(map(int,input().split())))
    S, G = map(int,input().split())
    for n1, n2 in arr:
        q[n1].append(n2)
        q[n2].append(n1)
    result = nodes(V,E,S,G,q)
    print(f'#{tc} {result}')
    # print(V,E)
    # print(arr)
    # print(S,G)
    # print(q)
