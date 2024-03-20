import sys
sys.stdin = open("input.txt","r")

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    numbers = list(map(int,input().split()))
    numbers.sort()
    # print(numbers)
    print(f'#{tc} {numbers[N//2]}')