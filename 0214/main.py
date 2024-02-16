def f(i,k, s, t):# k개의 원소를 가진 배열 A, 부분집합 합이 t인 경우
    global cnt
    cnt+=1
    if s == t: # 모든 원소에 대해 결정하면
        for j in range(k):
            if bit[j]: # A[j]가 포함된 경우
                print(A[j], end=' ')
        print()
    elif i == k: # 모든 원소를 고려했으나 s!= t
        return

    elif s > t: # 고려한 원소의 합이 t 보다 큰 경우
        return
    else:
        bit[i] = 1
        f(i+1,k,s+A[i], t)
        bit[i] = 0
        f(i+1,k,s,t)


# def f(i,k,t):
#     global cnt
#     cnt+=1
#     if i==k: # 모든 원소에 대해 결정하면
#         ss = 0 #부분집합 원소의 합
#         for j in range(k):
#             if bit[j]: #A[i] 가 포함된 경우
#                 ss += A[j]
#         if ss ==t:
#             for j in range(k):
#                 if bit[j]:  # A[i] 가 포함된 경우
#                     print(A[j], end=' ')
#             print()
#     else:
#         # for j in range(1,-1,-1):
#         #     bit[i] = j
#         #     f(i+1,k,t)
#         bit[i] = 1
#         f(i+1, k, t)
#         bit[i] = 0
#         f(i+1,k, t)

N = 10
A = [1,2,3,4,5,6,7,8,9,10]
bit = [0] * N
cnt = 0
f(0,N,0,5)
print(f'{cnt}')