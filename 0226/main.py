'''

3
6
A B C D E F
4
JACK QUEEN KING ACE
5
ALAKIR ALEXSTRASZA DR-BOOM LORD-JARAXXUS AVIANA
'''

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = []
    arr = input().split()
    result_arr = [0] * len(arr)
    # print(arr)
    if N % 2 == 0:
        for i in range(N//2):
            result_arr[i*2] = arr[i]
            result_arr[i*2+1] = arr[N//2+i]
    else:
        for i in range(N//2+1):
            result_arr[i*2]=arr[i]
        for i in range(N//2):
            result_arr[i*2+1] = arr[N//2+1 +i]
    print(f'#{tc}', end=' ')
    print(*result_arr)