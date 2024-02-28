T = int(input())
for tc in range(1, T+1):
    print(f'#{tc}', end=' ')
    N = int(input())
    request = [list(map(int, input().split()))
               for _ in range(N)]
    # request.sort(key=lambda x: x)
    # request.sort(key=lambda x: x[0])
    # print(request)
    # request.sort(key=lambda x: (x[0], x[1]))
    # print(request)
    # request.sort(key=lambda x: -x[0])
    # print(request)
    # request.sort(key=lambda x: (x[0], -x[1]))
    # print(request)

    # 요소의 1번째 인덱싱 (종료 시간) 을 기준으로 오름차순
    request.sort(key=lambda x: x[1])
    # print(request)
    # 맨 처음 회의는 어차피 받고 시작해야함
    end_time = request[0][1]  # 첫번째 e.
    cnt = 1
    for s, e in request:
        if end_time <= s:  # 새로운 화물차 시간이
            # 우리가 이전에 기록해놓은 종료시간 이상이라면
            cnt += 1
            end_time = e  # 새로운 시간으로 갱신시켜줌
        # 이 경우만 신경쓰면 됨
        # 어차피 정렬했기 때문에 다른 조건은 있을 수 없음
    print(cnt)