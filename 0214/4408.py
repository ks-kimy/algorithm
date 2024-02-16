#자기 방으로 돌아가기 => 재귀를 이용해서.
def back(i, k, lst): # k는 방의 갯수. i 는 시작지점.
    global min_mine
    global counting
    counting+=1
    if i == k:
        cnt = 1 # 초기값은 1초로 설정.
        temp_lst = [0,0]
        # print(lst) # 여기 까지 모든 순열이 이루어졌음. 여기서부터 계산하면 됨.
        for temp in lst:
            # print(temp)
            if temp[0] < temp_lst[0] < temp[1] or temp_lst[0]< temp[0] < temp_lst[1]:
              # 만약에 겹치는 라인이라면, cnt+ 1
              #   print('ok')
                temp_lst = temp
                # print(temp_lst , 'da')
                cnt += 1
            else:
                temp_lst =temp
                # print(temp_lst, 'fdsa')
                continue
        if min_mine > cnt:
            min_mine = cnt



    else:
        for j in range(i,k): # i 번째 방과 변경.
            lst[i], lst[j] = lst[j], lst[i]
            back(i+1,k,lst)
            lst[i], lst[j] = lst[j], lst[i]

    return min_mine, counting



T = int(input())

for tc in range(1, T+1):
    N = int(input())
    min_mine = N # 길이는 무조건 최대 시간이다.
    counting = 0
    numbers = [i for i in range(N)] # 방순서 첫번째 방 0, 두번째 방 1 ...
    rooms = [list(map(int, input().split())) for _ in range(N)]
    result = back(0,N,rooms)
    print(f'#{tc} {result}')