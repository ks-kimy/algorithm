
import sys
sys.stdin = open("input.txt","r")

def dfs(month, payment):
    global result
    if month > 12:
        if result > payment:
            result = payment
        return
    
    dfs(month+1, payment + cases[0] * months[month] )

    dfs(month+1, payment + cases[1])
    dfs(month+3, payment + cases[2])
    dfs(month+12, payment + cases[3])

T= int(input())
for tc in range(1,T+1):
    cases = list(map(int,input().split()))
    months = [0] + list(map(int, input().split()))
    result = 10000000
    print(f'#{tc}', end=' ')
    dfs(1,0)
    # print(cases)
    # print(months)
    print(result)