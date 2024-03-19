import sys
sys.stdin = open("input.txt","r")

def binary(start,end,num,check):
    global result
    if start > end :
        result = False
        return 

    middle = (start + end)//2
    if num < A[middle]:
        if check == 'left':
            result = False
            return
        binary(start,middle-1,num,'left')
    elif num > A[middle]:
        if check == 'right':
            result = False
            return
        binary(middle+1, end, num,'right')
    elif num == A[middle]:
        return

'''
def binary(start,end,num,check):
    global result
    if start == end and A[start] != num :
        result = False
        return 
    if check == 2 or check == -2:
        result = False
        return

    middle = (start + end)//2
    if num < A[middle]:
        binary(start,middle-1,num,check-1)
    elif num > A[middle]:
        binary(middle+1, end, num,check+1)
    elif num == A[middle]:
        return
이렇게 쓰면 안되는게 만약 오른쪽 왼쪽 왼쪽으로 가게되면 1->0->-1 이 된다...
그렇기 때문에 오류뜸...
'''

T= int(input())

for tc in range(1,T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    length_A = len(A)
    length_B = len(B)
    cnt = 0
    for b in B:
        result = True
        binary(0,length_A-1,b,'start')
        if result:
            cnt += 1
            print(b)

    print(f'#{tc} {cnt}')
