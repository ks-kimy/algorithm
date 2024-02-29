import sys
sys.stdin = open("input.txt", 'r')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    corridor = [0] * 400
    max_v = 0

    for _ in range(N):
        s, e = map(int, input().split())
        if s % 2 == 0: s -=1
        if e % 2 == 0: e -=1
        
        if s > e : s, e = e, s

        for i in range(s, e+1):
            corridor[i] += 1
    print(f'#{tc} {max(corridor)}')