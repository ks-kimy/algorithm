def frog_jump(arr):
    temp_sum = 0
    position = 0
     #이전 위치 값 저장 용도.
    direction = 0
    for i in range(K): # K 번 점프. 계산

        if arr[position] > 0 and direction == 0:
            position += arr[position]
            direction =0 #방향 정방향
            # 현재 위치의 값이 양수이면서 이전의 이동방향이 정방향.

        elif arr[position] < 0 and direction == 0:
            # guiswo 위치의 값이 음수이면서 이전의 이동방향 정방향.
            temp = arr[position] #이동하기 전의 인덱스 위치의 값.
            position += arr[position]

            direction -= 1

        elif arr[position] > 0 and direction == -1:
            # 현재 위치의 값이 양수이면서 이전의 이동방향이 역방향
            position += arr[position] - temp

            direction = 0



        elif arr[position] < 0 and direction < 0 :
            # 현재 위치의 값이 음수이면서 이전의 이동방향이 한 번 역방향.
            temp = arr[position]
            position += arr[position]

            direction -= 1

        elif arr[position] > 0 and direction <= -2:
            position += -temp

            temp = 0
            direction = 0

        #만약 범주에서 벗어나면 return
        if 0<= position < N:
            temp_sum += arr[position]
        else :
            return temp_sum
    return temp_sum









T = int(input())
for tc in range(T):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    result = frog_jump(arr)
    print(f'#{tc+1} {result}')