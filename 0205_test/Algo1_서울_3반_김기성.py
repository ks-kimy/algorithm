def shot_game(matrix): #함수 설정을 통해 확장성과 함수형 코딩 작성.
    temp_sum = 0 #임시의 최댓값 담을 부분.
    di = [-1,0,1,0]
    dj = [0,1,0,-1]
    # 방향성에 대한 부분 위로, 오른쪽, 아래, 왼쪽
    for i in range(N):
        for j in range(N):
            max_sum = 0 # 초기값 설정
            for k in range(4):
                ni = i
                nj = j
                # ni,nj 는 i와 j 가 이후 di dj 로 방향성에 대한 변화값을 저장하기 위한 변수.
                # k 의 반복마다 원래 자리로 초기화 되어야 함.
                ni += di[k]
                nj += dj[k]
                if 0<= ni <N and 0<=nj<N: # ni, nj의 참 검증. 왜냐 행렬의 바깥으로 나가게 될 수 있기 때문에.
                    max_sum += matrix[ni][nj]
                elif ni>=N or ni<0 or nj>=N or nj<0: # 만약 행렬의 바깥으로 나가게 될 경우에는 max 값을 0으로 만들고
                    # break 를 걸어 for k 에 대한 반복문 종료.
                    max_sum = 0
                    break
            max_sum -= matrix[i][j] # 가운데 값 빼줌. 위의 행렬 바깥으로 나가게 됐을 경우에도 빼줘도 됨 . 왜냐하면 어차피
            # 음수가 되었을 때나 0일때나 max_sum 값은 0으로 유지되기 때문.
            if max_sum % 2 == 0:
                max_sum *= 2
            elif max_sum > 0:
                max_sum = max_sum
            elif max_sum <= 0:
                max_sum = 0
            # max_sum 의 짝수일 때와 양수일 때 음수일 때에 대한 max_sum 조건 적용.
            if temp_sum <max_sum:
                temp_sum = max_sum
            # 처음 temp_sum 값을 max_sum 값과 비교하여 max_sum 값이 더 크면 temp_sum 값을 갱신함.
    return temp_sum



T = int(input())

for tc in range(T):
    N = int(input())
    matrix = [list(map(int,input().split())) for _ in range(N)] # 행렬 받는 input

    result = shot_game(matrix)
    print(f'#{tc+1} {result}')

