#이진탐색
def make_tree(n):
    global cnt
    if n:
        make_tree(left[n])
        cnt += 1
        lst[n] = cnt
        make_tree(right[n])



T = int(input())

for tc in range(1,T+1):
    N = int(input())
    tree = [0] * (N+1)
    cnt = 0
    left = [0] * (N+1)
    right = [0] * (N+1)
    lst = [0] * (N+1)

    for i in range(2,N+1): #자식 노드를 기준으로
        par_num = i //2
        if i % 2 == 0:
            left[par_num] = i
        else:
            right[par_num] = i

    make_tree(1)
    print(f'#{tc} {lst[1]} {lst[N//2]}')