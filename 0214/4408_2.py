T = int(input())  # 테스트 케이스의 수를 입력받음

for tc in range(1, T+1):  # 각 테스트 케이스에 대해
    print(f'#{tc}', end=' ')  # 테스트 케이스 번호 출력
    print()
    N = int(input())  # 구간의 수를 입력받음
    arr = [list(map(int,input().split())) for _ in range(N)]  # 각 구간의 시작과 끝을 입력받음
    answer = 0  # 겹치는 구간의 최대 수를 저장할 변수 초기화
    cnt = [0] * 201  # 각 위치에서 겹치는 구간의 수를 저장할 리스트 초기화

    for n1, n2 in arr:  # 각 구간에 대해
        print(n1,n2)
        if n1 < n2:  # 시작이 끝보다 작다면
            s = (n1 + 1) // 2  # 시작 위치 계산
            e = (n2 + 1) // 2  # 끝 위치 계산
            print(s,e,'fds')
        else:  # 끝이 시작보다 작다면
            e = (n1 + 1) // 2  # 끝 위치 계산
            s = (n2 + 1) // 2  # 시작 위치 계산
            print(s,e,'asda')


        for i in range(s, e+1):  # 시작 위치부터 끝 위치까지
            cnt[i] += 1  # 해당 위치에서 겹치는 구간의 수 증가

    print(max(cnt))  # 겹치는 구간의 최대 수 출력
