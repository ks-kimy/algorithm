#중위순회 영어로 in order
def in_order(T):
    global answer
    if T:
        in_order(left[T])
        answer+=words[T]
        in_order(right[T])


for tc in range(1,11):
    N = int(input())
    left = [0] *(N+1)
    right = [0] *(N+1)
    par = [0] * (N+1)
    words = [0] * (N+1)
    for i in range(N):
        line = input().split()
        # print(line)'/'
        if len(line) == 4:
            left[int(line[0])] = int(line[2]) # 부모 인덱스로 왼쪽 자식 노드 저장
            right[int(line[0])] = int(line[3]) # 부모 인덱스로 오른쪽 자식 노드 저장
            words[int(line[0])] = line[1] #문자 저장
            par[int(line[2])] = int(line[0])
            par[int(line[3])] = int(line[0])
        elif len(line) ==3:
            left[int(line[0])] = int(line[2])  # 부모 인덱스로 왼쪽 자식 노드 저장
            words[int(line[0])] = line[1]  # 문자 저장
            par[int(line[2])] = int(line[0])
        else:
            words[int(line[0])] = line[1] # 문자 저장

    # print(left,right,par,words)
    answer = ''
    in_order(1)
    print(f'#{tc} {answer}')