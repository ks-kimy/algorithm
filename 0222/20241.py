#이진수2
def bin2(n):
    temp = 0
    i = -1
    arr = ''
    while n:
        if n >= 2**i:
            n -= 2**i
            arr+='1'
            i -= 1
        elif n < 2**i:
            arr+='0'
            i -=1
        if len(arr)> 12:
            return 'overflow'
    return arr

T = int(input())
for tc in range(1, T+1):
    N = float(input())
    result = bin2(N)
    print(f'#{tc} {result}')