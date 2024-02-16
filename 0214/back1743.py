def void_food(arr):
    visited_length = 0
    max_num = 0
    di = [1, -1, 0, 0]
    dj = [0, 0, 1, -1]

    for row, col in arr:
        visited = [[row, col]]
        st = []
        cnt = 0

        while True:
            for k in range(4):
                if [row + di[k], col + dj[k]] in arr and [row + di[k], col + dj[k]] not in visited:
                    st.append([row, col])
                    row += di[k]
                    col += dj[k]
                    visited.append([row, col])
                    break

            if k == 3:
                if st:
                    [row, col] = st.pop()
                else:
                    break

        length = len(visited)
        if max_num < length:
            max_num = length

    return max_num

# 입력 받기
N, M, K = map(int, input().split())
arr = []
for _ in range(K):
    arr.append(list(map(int, input().split())))

# 함수 호출하여 결과 출력
result = void_food(arr)
print(result)
