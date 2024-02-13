'''
fx = (6+5*(2-8)/2)
'''

top = -1
stack = [0]*100

icp = {'(':3 , '*': 2, '/': 2 , '+' :1 , '-':1}
isp = {'(':0 , '*': 2, '/': 2 , '+' :1 , '-':1}

fx = '(6+5*(2-8)/2)'
postfix = ''
for tk in fx:
    # 여는 괄호 push, 연산자이고 top 원소보다 우선순위보다 높으면 push
    if tk == '(' or (tk in '*/+-' and isp[stack[top]] < icp[tk]):
        top += 1 #push
        stack[top] = tk
    elif tk in '*/+-' and isp[stack[top]] >= icp[tk]:    # 연산자이고 top 원소보다 우선순위가 높지 않으면
        while isp[stack[top]] >= icp[tk]: # top 원소보다 우선순위가 낮을 때까지 pop
            top -= 1 # pop
            postfix += stack[top+1]
    elif tk == ')': # 닫는 괄호면, 여는 괄호를 만날때까지 pop
        while stack[top]!= '(':
            top -=1
            postfix += stack[top+1]
        top -= 1
        stack[top+1] =tk
    else:
        postfix += tk
print(postfix)