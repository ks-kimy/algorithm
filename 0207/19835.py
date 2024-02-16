T = int(input())  # 테스트 케이스의 수를 입력받습니다.

st = []  # 스택을 초기화합니다.
def push(data):  # 스택에 데이터를 추가하는 함수입니다.
    st.append(data)
def pop():  # 스택에서 데이터를 제거하는 함수입니다.
    return st.pop()

for tc in range(1, T+1):  # 각 테스트 케이스에 대해 반복합니다.
    st.clear()  # 스택을 비웁니다.
    text = input()  # 괄호 문자열을 입력받습니다.
    print(f'#{tc}', end=' ')  # 테스트 케이스 번호를 출력합니다.
    for c in text:  # 문자열의 각 문자에 대해 반복합니다.
        # 괄호의 종류에 따라 스택에 추가하거나 제거합니다.
        if c == '{':
            push('{')
        if c == '(':
            push('(')
        if c == ')':
            if st and st[-1] == '(':
                pop()
            else:
                push(')')
        if c == '}':
            if st and st[-1] == '{':
                pop()
            else:
                push('}')

    else:
        print(1 if not st else 0)  # 스택이 비어있으면 1(올바른 괄호), 그렇지 않으면 0(올바르지 않은 괄호)을 출력합니다