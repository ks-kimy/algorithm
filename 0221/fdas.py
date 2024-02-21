def calculate(n_th_vertex):
    current_v = vertexes[n_th_vertex]
    if len(current_v) == 2:
        return int(current_v[1])

    if current_v[1] == '+':
        return calculatev[2])) (int(current_+ calculate(int(current_v[3]))
    if current_v[1] == '-':
        return calculate(int(current_v[2])) - calculate(int(current_v[3]))
    if current_v[1] == '*':
        return calculate(int(current_v[2])) * calculate(int(current_v[3]))
    if current_v[1] == '/':
        return calculate(int(current_v[2])) / calculate(int(current_v[3]))


for tc in range(1, 11):
    N = int(input())
    vertexes = [0] * (N + 1)

    for _ in range(N):
        vertex = input().split()
        print(vertex)
        n_th_vertex = int(vertex[0])
        vertexes[n_th_vertex] = vertex
        print(vertexes)
    # print(f'#{tc} {int(calculate(1))}')