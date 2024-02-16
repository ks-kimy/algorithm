T = 10


# 브루트포스 - 고지식한 알고리즘

def bf(pattern, text):
    len_t = len(text)
    len_p = len(pattern)
    i = 0  # 전체 텍스트에서 탐색에 쓸 인덱스
    j = 0  # 패턴 탐색에 쓸 인덱스
    # i = j = 0
    count = 0 # 전체 단어가 존재하는 횟수
    while i < len_t and j < len_p:
        # 현재 탐색하고 있는 문자와 해당 위치와
        # 대응되는 패턴 문자가 다를 때
        if text[i] != pattern[j]: # 탐색 실패
            i = i - j
            j = -1
        i += 1
        j += 1
        # 패턴을 만족시켰을 때
        if j == len_p:  # len_p -1까지 탐색 완료
            # 개별 위치 찾을 때 : 인덱스를 리턴 -> i - len_p
            count += 1
            i = i - j + 1
            j = 0
    return count


for _ in range(T):
    tc = input()
    pattern = input()
    text = input()
    result = bf(pattern, text)
    print(f'#{tc} {result}')