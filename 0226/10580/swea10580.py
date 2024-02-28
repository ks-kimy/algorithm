'''
2
3
1 10
5 5
7 7
2
1 1
2 2
'''
def pole():
    #리스트 arr : 튜플 형태로 a 전봇대와  b 전봇대를 저장할 리스트
    size = len(arr)
    cnt = 0
    for i in range(size):
        for tar in range(i):
            # a 전봇대 : 튜플의 첫번째 요소, b 전봇대 :  튜플의 두번째 요소
            i_a, i_b = (arr[i][0], arr[i][1])
            tar_a , tar_b = (arr[tar][0], arr[tar][1])
            if i_b < tar_b:
                cnt += 1
    return cnt


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    result = pole()
    print(f'# {tc} {result}')
    # print(arr)