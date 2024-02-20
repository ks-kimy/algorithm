def sum_nodes(node):  # 출력할 node의 번호를 받아서 그 노드를 기준으로 자식 노드들의 값을 합산하는 함수입니다.
    global prices  # 전역 변수 prices를 사용하기 위해 global 키워드를 사용합니다.
    if node:  # 현재 노드가 있는 경우에만 수행합니다.
        sum_nodes(left[node])  # 왼쪽 자식 노드를 기준으로 재귀 호출합니다.
        sum_nodes(right[node])  # 오른쪽 자식 노드를 기준으로 재귀 호출합니다.

        # 현재 노드에 왼쪽 자식 노드의 가격을 더합니다.
        if left[node] != 0:  # 왼쪽 자식 노드가 있는 경우에만 수행합니다.
            prices[node] += prices[left[node]]

        # 현재 노드에 오른쪽 자식 노드의 가격을 더합니다.
        if right[node] != 0:  # 오른쪽 자식 노드가 있는 경우에만 수행합니다.
            prices[node] += prices[right[node]]


T = int(input())  # 테스트 케이스의 개수를 입력받습니다.
for tc in range(1, T + 1):
    N, M, L = map(int, input().split())  # 노드의 개수 N, 리프 노드의 개수 M, 출력할 노드 번호 L을 입력받습니다.
    left = [0] * (N + 1)  # 각 노드의 왼쪽 자식 노드를 저장하기 위한 리스트를 초기화합니다.
    right = [0] * (N + 1)  # 각 노드의 오른쪽 자식 노드를 저장하기 위한 리스트를 초기화합니다.
    prices = {i: 0 for i in range(1, N + 1)}  # 각 노드의 가격을 저장하는 딕셔너리를 초기화합니다.

    # 리프 노드의 가격을 입력받아 prices 딕셔너리에 저장합니다.
    for _ in range(M):
        key, value = map(int, input().split())
        prices[key] = value

    # 각 노드의 부모-자식 관계를 left와 right 리스트에 저장합니다.
    for i in range(2, N + 1):
        par_index = i // 2
        if i % 2 == 0:
            left[par_index] = i
        else:
            right[par_index] = i

    sum_nodes(1)  # 루트 노드(1번 노드)를 기준으로 자식 노드들의 값을 합산합니다.
    print(f'#{tc} {prices[L]}')  # 출력할 노드 L의 가격을 출력합니다.
