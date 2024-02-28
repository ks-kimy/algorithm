T = int(input())  # 테스트 케이스의 수를 입력 받음

# 16진수를 2진수로 변환하는 딕셔너리
hex_to_bin = {
    '0': '0000', '1': '0001', '2': '0010', '3': '0011',
    '4': '0100', '5': '0101', '6': '0110', '7': '0111',
    '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
    'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'
}

# 암호 패턴을 숫자로 변환하는 딕셔너리
pattern_dict = {
    '211': 0, '221': 1, '122': 2, '411': 3, '132': 4,
    '231': 5, '114': 6, '312': 7, '213': 8, '112': 9,
}

# 각 테스트 케이스에 대해
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # 행렬의 크기를 입력 받음
    matrix = [input().strip() for _ in range(N)]  # 행렬을 입력 받음

    matrix_set = list(set(matrix))  # 중복을 제거한 행렬을 생성
    N2 = len(matrix_set)  # 중복을 제거한 행렬의 크기

    binary_codes = []  # 2진수 코드를 저장할 리스트
    for i in range(N2):
        tmp = ''  # 임시 문자열
        for j in range(M):
            tmp += hex_to_bin[matrix_set[i][j]]  # 16진수를 2진수로 변환
        if int(tmp, 2):  # 2진수가 0이 아니라면
            binary_codes.append(tmp)  # 리스트에 추가

    result = 0  # 결과값
    visited = []  # 방문한 코드를 저장할 리스트
    for binary_code in binary_codes:  # 각 2진수 코드에 대해
        decode = []  # 해독된 코드를 저장할 리스트
        # 암호 비율
        a = b = c = d = 0
        binary_code = binary_code.rstrip('0')  # 오른쪽의 0을 제거
        L = len(binary_code)  # 2진수 코드의 길이
        # binary_code를 뒤로부터 검토
        for i in range(L - 1, -1, -1):
            # 맨끝에서 연속중인 1을 카운팅
            if c == 0 and binary_code[i] == '1':
                d += 1
            # 1 다음에 오는 0을 카운팅
            elif d > 0 and b == 0 and binary_code[i] == '0':
                c += 1
            # 0 다음에 오는 1을 카운팅
            elif a == 0 and binary_code[i] == "1":
                b += 1
            # 0을 만났기 때문에 지금까지의 기록을 디코딩
            elif b > 0 and c > 0 and d > 0 and binary_code[i] == '0':
                div = min(b, c, d)
                b //= div
                c //= div
                d //= div
                key = str(b) + str(c) + str(d)
                decode.insert(0, pattern_dict[key])
                a = b = c = d = 0

            # 해독된 코드의 길이가 8이라면
            if len(decode) == 8:
                # 해독된 코드가 유효하다면
                if ((decode[0] + decode[2] + decode[4] + decode[6]) * 3 + decode[1] + decode[3] + decode[5] + decode[7]) % 10 == 0:
                    # 해독된 코드가 방문한 코드 리스트에 없다면
                    if decode not in visited:
                        result += sum(decode)  # 결과값에 더함
                        visited.append(decode)  # 방문한 코드 리스트에 추가
                decode = []  # 해독된 코드 리스트를 초기화
    print(f"#{tc} {result}")  # 결과 출력