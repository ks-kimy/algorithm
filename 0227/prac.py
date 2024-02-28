# nCr 짜보자
N = 5
K = 3
arr = [0]*K
A = [1,2,3,4,5]
def comb(level,S):
    if level == K:
        print(arr)
        return
    for i in range(S, N-K+level+1):
        arr[level] =A[i]
        comb(level+1, i+1)
comb(0,0)