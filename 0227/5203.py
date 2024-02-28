T = int(input())

# 이겼는지 체크를 위한 함수
def check(player):
    # 10장을 돌면서검사
    for j in range(10):
        # 만약 같은 카드를 3장 가지고 있으면 이겼음
        if player[j] == 3:
            return True
    # 마지막 7,8,9 까지만 검사
    for k in range(8):
        # 연속된다면 이겼으니까 종료
        if player[k] and player[k + 1] and player[k + 2]:
            return True
    # 승리요건 달성 못함
    return False


for tc in range(1, T + 1):
    cards = list(map(int, input().split()))

    # 각각의 인덱스가 카드번호가 되도록 플레이어들 초기값 생성
    p1 = [0] * 10
    p2 = [0] * 10
    # 처음 시작은 비기는 걸로
    winner = 0

    # 주어진 카드를 한장씩 나눠주자
    for i in range(len(cards)):
        # 먼저 p1부터 받는다. (짝수)
        if not i % 2:
            # 카드 번호에 해당하는 p1의 인덱스에 카드 장수를 늘려준다.
            p1[cards[i]] += 1
            # 승리조건을 만족했다면
            if check(p1):
                # 승자! 후 종료
                winner = 1
                break
        else:
            # p2도 p1과 같이 동일한 검정 과정
            p2[cards[i]] += 1
            if check(p2):
                winner = 2
                break

    print(f"#{tc} {winner}")