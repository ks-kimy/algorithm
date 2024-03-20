import sys
from collections import deque
sys.setrecursionlimit(200000)
sys.stdin = open("input.txt", "r")


def lca_p(): #  자식 c에 대한 2^k 번째 부모 
    for k in range(1,max):
        for c in range(1,N+1):
            parents_arr[k][c] = parents_arr[k-1][parents_arr[k-1][c]]


def depth_same(a,b):  # 깊이를 갖게 만들어주는 함수. 
    a_depth = depth[a]
    b_depth = depth[b]
    if a_depth < b_depth:
        a_depth, b_depth = b_depth, a_depth 
        a,b = b, a
    if a_depth ==  b_depth:
        return a,b
    differ = a_depth - b_depth
    K = 0
    while True:
        if 2**K < differ:
            K += 1
        if 2**K > differ:
            K -= 1
            break
        if 2**K == differ:
            break
    # differ 보다 작지만 가장 큰 2^K 의 K 값 구하기
    while a_depth != b_depth:
        if depth[parents_arr[K-1][a]] > depth[b]:
            a = parents_arr[K-1][a]        
            K -= 1 
            # 만약 a의 2^(K-1)번째 조상의 깊이가 b 의 깊이보다 깊다면      
        elif depth[parents_arr[K-1][a]] < depth[b]:
            K -= 1
        elif depth[parents_arr[K-1][a]] == depth[b]:
            return parents_arr[K-1][a], b

        


        

def lca(a,b): #여기서는 공통 조상 return
    # b 를 기준으로 짠다. b 가 큰 것.
    a,b = depth_same(a,b) # a와 b 는 depth가 같다. 
    #깊이가 같아지거나 높아질때까지.
    if a == b :
        return a
    if depth[a] == 1:
        return parents_arr[0][a]
    #깊이가 1이면 바로 위. 밑의 else 부분에서 오류가 난다. 왜냐하면 깊이가 1이기 때문에 ancestor가 0이 될 때까지 If 문을 순회하기 때문이다. 
    for ancestor in range(max-1,-1,-1):
        if parents_arr[ancestor][a] != parents_arr[ancestor][b]:
            a = parents_arr[ancestor][a]
            b = parents_arr[ancestor][b]
    return parents_arr[0][a]       
        

def bfs(start):
    q = deque()
    q.append(start)

    while q:
        
        before_node = 0
        node = q.popleft()
        # result = lca(before_node, node)
        bfs_arr.append(node)
        visited[node] = 1

        for c in connection[node]: # c 는 child의 약자. 즉 부모의 자식을 의미한다. 이때 부모는 node 이다. 
            if visited[c] == 0:
                q.append(c)
                parents_arr[0][c] = node
                depth[c] = depth[node] + 1
                visited[c] = 1





T = int(input())
for tc in range(1, T+1):
    N = int(input())
    max = 20
    connection = [[] for _ in range(N+1)]
    depth = [0 for _ in range(N+1)] # 각 노드의 깊이를 다 기록해둔다. 
    parents_arr = [[0] * (N+1) for _ in range(max)] # 각각의 index에서 2^0, 2^1, 2^2 ... 순서대로 부모를 저장해둔다. [[][][][][][][][][][][][]] 첫번째를 시작으로 1,2,4,8 ~~ 번째 부모들을 나타냄.
    # 그리고 그 안에의 인덱스들은 그 해당인덱스의 부모를 나타냄. ex) [[0,0,1,1,3,3,2,4,1,3,2,9][0,0,0,0,1,1,1,3,0,1,1,3]] 첫번째 리스트는 1번째 부모들에 대한 표현 0,1,2,3,4 순으로 인덱스에 대한 표현
    # 그 인덱스의 값이 부모를 의미. 또한 두 번째 리스트는 1번째(2^1번째) 의 부모를 의미. 
    visited = [0 for _ in range(N+1)]
    parents = list(map(int, input().split()))
    bfs_arr = []
    for i in range(len(parents)):
        parent = parents[i]
        child = i+2
        connection[parent].append(child)
        connection[child].append(parent)
    # print(f'#{tc}')
    # print(f'parent = {parents} node 2,3,4,5,~~ 순으로 진행') # node 2,3,4,5,~~ 순으로 진행
    # print(f'connection = {connection}')
    bfs(1)
    # print(f'bfs로 진행했을 때 출력되는 순서 = {bfs_arr}')
    # print(f'depth = {depth}')
    lca_p()
    # print(parents_arr)
    # print(parents_arr[k][n-1])
    result = 0
    re = 0
    for i in range(1,N):
        same = lca(re,bfs_arr[i])
        d_same = depth[same]
        d_re = depth[re]
        d_bfsi = depth[bfs_arr[i]]
        result += (d_re-d_same + d_bfsi - d_same)
        re = bfs_arr[i]
    print(f'#{tc} {result}') 