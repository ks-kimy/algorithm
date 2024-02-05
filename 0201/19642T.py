T = int(input())  # 테스트 케이스의 수를 입력받습니다.

def selection_sort(data):
    for i in range(0, len(data)):  # 데이터의 각 요소에 대해
        target_idx = i  # 현재 인덱스를 타겟 인덱스로 설정합니다.
        for j in range(i + 1, len(data)):  # 현재 인덱스 이후의 모든 요소에 대해
            if i % 2:  # 인덱스가 홀수인 경우 -> 오름차순
                if data[target_idx] > data[j]:  # 현재 타겟 값이 다음 요소보다 크면
                    target_idx = j  # 타겟 인덱스를 j로 업데이트합니다.

            else:  # 인덱스가 짝수인 경우 -> 내림차순
                if data[target_idx] < data[j]:  # 현재 타겟 값이 다음 요소보다 작으면
                    target_idx = j  # 타겟 인덱스를 j로 업데이트합니다.

        data[i], data[target_idx] = data[target_idx], data[i]  # 타겟 인덱스의 요소와 현재 인덱스의 요소를 교환합니다.
    return arr[:10]  # 정렬된 배열의 처음 10개 요소를 반환합니다.

for tc in range(1, T+1):  # 각 테스트 케이스에 대해
    N = int(input())  # 숫자의 개수를 입력받습니다.
    arr = list(map(int, input().split()))  # 숫자들을 입력받아 리스트로 만듭니다.
    print(f'#{tc} {" ".join(map(str, selection_sort(arr)))}')  # 선택 정렬을 수행하고 결과를 출력합니다.