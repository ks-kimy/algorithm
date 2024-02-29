import sys
sys.stdin = open('sample_input(1).txt', 'r')

T = int(input())  # 테스트 케이스의 수를 입력받습니다.
for tc in range(1, T+1):  # 각 테스트 케이스에 대해
    print(f'#{tc}', end=' ')  # 테스트 케이스 번호를 출력합니다.
    N, M = map(int, input().split())  # 보드의 크기와 돌을 놓는 횟수를 입력받습니다.
    answer1 = answer2 = 0  # 각 색깔의 돌 개수를 저장하는 변수를 초기화합니다.
    board = [[0] * N for _ in range(N)]  # 보드를 초기화합니다.
    mid = N // 2  # 보드의 중앙 위치를 계산합니다.
    # 게임 시작 시 중앙에 놓이는 돌을 설정합니다.
    board[mid - 1][mid - 1] = 2
    board[mid - 1][mid] = 1
    board[mid][mid - 1] = 1
    board[mid][mid] = 2
    # 8방향을 나타내는 델타값을 설정합니다.
    di = [-1, -1, 1, 1, 1, -1, 0, 0]
    dj = [-1, 1, -1, 1, 0, 0, 1, -1]
    for _ in range(M):  # 돌을 놓는 횟수만큼 반복합니다.
        i, j, color = map(int, input().split())  # 돌을 놓을 위치와 색깔을 입력받습니다.
        i -= 1
        j -= 1
        board[i][j] = color  # 돌을 놓습니다.
        change = []  # 뒤집을 돌의 위치를 저장하는 리스트를 초기화합니다.
        for k in range(8):  # 8방향에 대해
            ni = i + di[k]
            nj = j + dj[k]
            while True:  # 해당 방향으로 계속 이동하며
                if not (0 <= ni < N and 0 <= nj < N):  # 보드를 벗어나면
                    change.clear()  # 뒤집을 돌의 위치를 초기화하고
                    break  # 반복문을 종료합니다.
                if board[ni][nj] == 0:  # 빈 칸을 만나면
                    change.clear()  # 뒤집을 돌의 위치를 초기화하고
                    break  # 반복문을 종료합니다.
                if board[ni][nj] == color:  # 같은 색의 돌을 만나면
                    break  # 반복문을 종료합니다.
                change.append((ni, nj))  # 뒤집을 돌의 위치를 추가합니다.
                ni += di[k]
                nj += dj[k]

            for cx, cy in change:  # 뒤집을 돌의 위치에 대해
                board[cx][cy] = color  # 돌의 색을 바꿉니다.

    answer1 = sum([row.count(1) for row in board])  # 1번 색깔의 돌 개수를 계산합니다.
    answer2 = sum([row.count(2) for row in board])  # 2번 색깔의 돌 개수를 계산합니다.
    print(answer1, answer2)  # 각 색깔의 돌 개수를 출력합니다.