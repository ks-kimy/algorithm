# 이진 힙
def enq(n):
    global last
    last+=1 # index 에 대한 부분
    tree[last] = n # 인덱스에 들어가는 것.
    temp = n
    c = last
    p = last//2
    while p >=1 and tree[c] < tree[p]: #부모가 존재하고 자식이 부모보다 작으면
        tree[c], tree[p] =  tree[p], tree[c]
        c = p
        p = c//2
def sum_heap(n): # 마지막 노드 n
    p = n//2
    global sum_
    while p>=1:
        sum_ += tree[p]
        p //= 2
    return sum_

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    tree = [0] * (N+1)
    last = 0
    sum_ = 0
    for i in arr:
        enq(i)
    result = sum_heap(N)
    print(f'#{tc} {result}')