#이진탐색
def make_tree(n):
    global cnt
    if n:
        cnt -=1





T = int(input())

for tc in range(1,T+1):
    N = int(input())
    tree = [0] * (N+1)
    cnt = N
    left = [0] * (N+1)
    right = [0] * (N+1)
    for i in range(1,N+1):
        l_num = i*2
        r_num = i*2 + 1
        left[i] = l_num
        right[i] = r_num

