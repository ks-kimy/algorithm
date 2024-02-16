#피자굽기
from collections import deque
def pizza(N,M,pizzas):
    plate = deque(pizzas[:N]) #처음 plate N 개 만큼 할당
    pizzas = deque(pizzas)
    for _ in range(N):
        pizzas.popleft()

    while len(plate) > 1:
        plate[0][0] = plate[0][0]//2
        if plate[0][0] != 0:
            plate.rotate(-1)
        elif plate[0][0] == 0 and pizzas : #plate[0] 번째가 0이고 pizzas 가 존재할 때
            plate[0] = pizzas.popleft()
            plate.rotate(-1)
        else:
            plate.popleft()

    return plate[0][1]



T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    arr = []
    ci = list(map(int, input().split()))
    for i in range(M):
        arr.append([ci[i],i+1])
    # print(arr)
    result = pizza(N,M,arr)
    print(f'#{tc} {result}')