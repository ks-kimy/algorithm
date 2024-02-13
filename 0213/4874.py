T = int(input())
for tc in range(1, T+1):
    print(f'#{tc}', end=' ')
    arr = input().split()
    answer = 0
    st = []

    for a in arr:
        #전달받은 계산식을 앞으로부터 탐색
        #이미 후위식으로 되어 있으니 계산만
        # 1. 숫자는 스택에 넣는다.
        # 2. 연산자는...
        if a not in ['+','-', ' *', '/']:
            st.append(int(a))
        else: #연산자일 경우
            if a == '.':
                continue
            if len(st) < 2:
                print('error')
                break
            pop1 = st.pop()
            pop2 = st.pop()
            if a =='+':
                st.append(pop2 + pop1)
            elif a =='-':
                st.append(pop2-pop1)
            elif a =='*':
                st.append(pop2*pop1)
            elif a =='/':
                st.append(pop2//pop1)

    else :
        print(st[-1] if len(st) == 1 else 'error')