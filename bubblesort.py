T = 10  # 테스트 케이스의 수를 설정합니다.

for tc in range(1, T+1):  # 각 테스트 케이스에 대해 반복합니다.
    print(f'#{tc}', end=' ')  # 현재 테스트 케이스 번호를 출력합니다.
    _ = input()  # 불필요한 입력을 무시합니다.
    arr = list(map(int, input().split()))  # 노드 연결 정보를 입력받아 정수 리스트로 변환합니다.
    connect = [[] for _ in range(100)]  # 각 노드에 연결된 노드를 저장할 리스트를 초기화합니다.
    for i in range(0, len(arr), 2):  # 입력받은 연결 정보를 통해 그래프를 구성합니다.
        connect[arr[i]].append(arr[i+1])
    result = 0  # 결과를 저장할 변수를 초기화합니다. 0은 목표 노드에 도달하지 못했음을, 1은 도달했음을 나타냅니다.
    st = [0]  # 탐색을 시작할 노드를 스택에 넣습니다.
    node = nxt = 0  # 현재 노드와 다음 노드를 0으로 초기화합니다.
    while st and nxt != 99:  # 스택이 비어있지 않고, 목표 노드에 도달하지 않았다면 계속 탐색을 진행합니다.
        node = st.pop()  # 스택에서 노드를 하나 꺼내 탐색을 진행합니다.
				for nxt in connect[node]:  # 현재 노드에 연결된 노드의 탐색을 진행합니다.
            if nxt == 99:  # 꺼낸 노드가 목표 노드라면 결과를 1로 설정하고 탐색을 종료합니다.
                result = 1
                break
            st.append(nxt)  # 꺼낸 노드를 스택에 넣어 다음 탐색을 준비합니다.
    print(result)  # 결과를 출력합니다.