import sys
sys.stdin = open("input.txt","r")

def payment():
    for i in range(1, 13):
        nmin = pay[i-1] + months[i] * cases[0]  

        nmin = min(nmin, pay[i-1] + cases[1])

        if i >=3:
            nmin = min(nmin, pay[i-3] + cases[2])
        if i >=12:
            nmin = min(nmin, cases[3])
        
        pay[i] = nmin
T= int(input())

for tc in range(1,T+1):
    cases = list(map(int,input().split()))
    months = [0] + list(map(int, input().split()))
    pay = [0 for _ in range(13)]
    payment()
    print(f'#{tc}', end=' ')
    # print(cases)
    # print(months)
    print(pay[12])