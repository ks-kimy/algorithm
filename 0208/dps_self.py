'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''
def dfs(i):  # 시작 i , 마지막, V
    visited[i] = 1  #방문표시
    print(i)
    # i 에 인접하고 방문 안한 w가 있으면
    for w in adjl[i]:
        if visited[w] == 0:
            dfs(w)




V, E = map(int, input().split())
arr = list(map(int, input().split()))

# 인접리스트
adjl = [[] for _ in range(V+1)] #ardjl[i]행에 i 에 인접인 정점번호.
# print(V)
# print(E)
# print(arr)
for i in range(E):
    n1, n2 = arr[i*2], arr[i*2 + 1]
    # print(n1,n2)
    adjl[n1].append(n2)
    adjl[n2].append(n1) # 방향이 없는 경우
print(adjl)
visited = [0] * (V + 1)  # visited, stack 생성 및 초기화

dfs(1)