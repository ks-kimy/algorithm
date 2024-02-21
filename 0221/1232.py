# 사칙연산
from collections import deque
def operation(T):
    if T: # 이 때 T 는 부모 노드.
        operation(left[T])
        operation(right[T])
        op = operator[T]
        if str(op) not in '-+*/': #숫자라면
            numbers[T] = op #넘버스에다 숫자 저장.
            return
        temp1 = numbers[left[T]]
        temp2 = numbers[right[T]]
        if op == '-':
            temp = temp1 - temp2
        elif op == '+':
            temp = temp1 + temp2
        elif op =='*':
            temp = temp1 * temp2
        elif op == '/':
            temp = temp1 // temp2
        numbers[T] = temp



for tc in range(1,11):
    N = int(input())
    left = [0] * (N+1)
    right = [0] * (N+1)
    operator = [0] * (N+1) #모든 것들 답는 것.
    numbers = [0] * (N+1) #숫자들을 담는 것. 또한 계산 값들도.
    # result = deque()
    for _ in range(N):

        arr = input().split()

        if len(arr) == 4:
            # left[arr[0]]
            num = int(arr[0])
            oper = arr[1]
            left_c = int(arr[2])
            right_c = int(arr[3])
            left[num] = left_c
            right[num] = right_c
            operator[num] = oper

        else:
            num = int(arr[0])
            number = int(arr[1])
            # print(number)
            operator[num] = number
    print(left)
    print(right)
    operation(1)
    print(numbers)
    print(f'#{tc}', numbers[1])

    # while len(result) != 1:
    #     temp1 = result.popleft()
    #     op = result.popleft()
    #     temp2 = result.popleft()
    #     if op == '-':
    #         temp = temp1 - temp2
    #     elif op == '+':
    #         temp = temp1 + temp2
    #     elif op =='*':
    #         temp = temp*temp2
    #     elif op == '/':
    #         temp = temp/temp2
    #     result.appendleft(temp)
    # final_result = result.pop()
    # print(int(final_result))