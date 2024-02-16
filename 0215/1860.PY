#진기의 최고급 붕어빵
from collections import deque
def fish_bread(N,M,K,arr): # N 명의 사람,M초동안 K개 생성
    arr.sort() # 순서대로 arr 정렬.
    arr = deque(arr)
    time = 0 #걸리는 시간
    nums = 0 #붕어빵의 갯수
    temp_arr = deque()
    '''
    나는 붕어빵의 갯수를 M초 뒤에 K 개를 만들 것이다. 
    그리고 사람이 정해진 시간 마다 들어오니 그 때마다 빼줄건데 어떻게 구현할 수 있을까?
    흠....
    
    
    '''
    while True:
        time +=1
        if time % M == 0:
            nums += K # M 초 마다 K 개 만큼 생김
        temp = arr.popleft()

        if time ==
        temp_arr.append(temp)
        if temp < M:
            return 'Impossible' # 만약 뽑아내는 것 중 M 보다 작은게 있다면 바로 불가능.


    return arr





T = int(input())
for tc in range(1, T+1):
    N,M,K = map(int,input().split())
    arr = list(map(int, input().split()))
    result = fish_bread(N,M,K,arr)