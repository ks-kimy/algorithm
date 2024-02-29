import sys
sys.stdin = open("input.txt", "r")

def start():
    sold_bread = 0
    for person in customers:
        # 공식, 특정시간에 만들 수 있는 빵의 갯수
        made_bread = (person // M) * K

        # 빵을 1개 팔았다.
        sold_bread += 1

        # 재고 계산
        remain = made_bread - sold_bread

        if remain < 0 :
            return 'Impossible'
    return 'Possible'
T = int(input())
for tc in range(1, T+1):
    N,M,K = map(int, input().split())
    customers = sorted(list(map(int,input().split())))
    result = start()
    print(f"#{tc} {result}")