




N = 10
q = [0]* N
front = rear = -1
# 큐 생성

rear +=1
q[rear] = 10
rear +=1
q[rear] = 20
rear +=1
q[rear] = 30
rear +=1
q[rear] = 40

while front != rear:
    front +=1
    print(q[front])

