def plus(N, arr):
    stack = []
    postfix = ''
    for word in arr:
        if word == '+':
            while stack:
                postfix += stack.pop()
            stack.append(word)
        else:
            postfix += word

    while stack:
        postfix += stack.pop()
    return postfix

T = 10
for tc in range(T):
    N = int(input())
    arr = input()
    stack = []
    result = plus(N, arr)
    # print(result)
    for word in result:
        if word != '+':
            stack.append(word)
        else:
            num2 = int(stack.pop())
            num1 = int(stack.pop())
            stack.append(num1+num2)
    print(f'#{tc+1} {stack[0]}')
