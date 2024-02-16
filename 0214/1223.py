# 계산기2
def calculator(length, arr):
    st = [] # 연산자 담는 스택
    form = '' # 후위표기식을 위한 빈 문자열
    top = -1 # 스택의 top의 인덱스를 표기하는 것.
    i = 0
    isp = {'+': 1 , '-':1, '*': 2, '/': 2} # in stack
    icp = {'+': 1 , '-':1, '*': 2, '/': 2} # incoming

    for word in arr:
        if top < 0 and word in '+-*/':
            st.append(word)

            top += 1


        elif word in '+-*/' and top >= 0 :
            if isp[st[top]] < icp[word]: # 들어오는게 스택에 들어있는 것 보다 우선순위가 높다면 푸시.
                st.append(word)
                top += 1
            else: # 들어오는게 스택에 들어있는 것보다 우선순위가 낮거나 같다면 높아질 때까지 팝 하고 form 에 합.
                while  top >= 0 and isp[st[top]] >= icp[word] :
                    top -= 1
                    form += st.pop()
                st.append(word)
                top += 1

        elif word not in '+-*/': #숫자라면
            form += word
    while st: # 남은 것들 모두 pop
        form += st.pop()
    return form
def calc(length, arr):
    st = []
    for word in arr:
        if word not in '+-*/':
            st.append(word)
        elif word == '+':
            num2 = int(st.pop())
            num1 = int(st.pop())
            st.append(str(num1+num2))
        elif word == '-':
            num2 = int(st.pop())
            num1 = int(st.pop())
            st.append(str(num1 - num2))
        elif word == '*':
            num2 = int(st.pop())
            num1 = int(st.pop())
            st.append(str(num1 * num2))
        else :
            num2 = int(st.pop())
            num1 = int(st.pop())
            st.append(str(num1 / num2))
    return st


T = 10

for tc in range(1, T+1):
    length = int(input())
    arr= input()
    # print(arr)
    result = calculator(length, arr)
    result2 =  calc(length,result)
    result3 = int(*result2)
    print(f'#{tc} {result3}')