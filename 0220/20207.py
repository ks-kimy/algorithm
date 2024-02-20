def numbering(T):
    global cnt
    if T:
        numbering(left[T])
        # print(cnt)
        numbers[T] = cnt
        cnt+=1
        numbering(right[T])

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    numbers = {i:0 for i in range(1,N+1)}
    cnt = 1
    #6개
    left = [0] * (N+1)
    right = [0] * (N+1)

    for i in range(2,N+1):
        par_num = i //2
        if i % 2 == 0:
            left[par_num] = i
        else:
            right[par_num] = i
    print(left, right)
    numbering(1)
    print(f'#{tc} {numbers[1]} {numbers[N//2]}')