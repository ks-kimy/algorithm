#subtree
def subtree(T):

    global cnt
    if left[T] != 0:
        subtree(left[T])
        cnt+=1
    if right[T] != 0:
        subtree(right[T])
        cnt+=1
    print(T, cnt)
T = int(input())

for tc in range(1,T+1):
    cnt = 1
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))
    left = [0]* (E+2)
    right = [0]* (E+2)
    par = [0] * (E+2)
    for i in range(E):
        p, c = arr[i*2], arr[i*2+1]
        if left[p] ==0:
            left[p] = c
        else:
            right[p] = c
        par[c] = p
    print(par)
    print(left,'left')
    print(right,'right')
    subtree(N)
    print(f'#{tc} {cnt}')