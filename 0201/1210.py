def direction_x(matrix):
    x = 0
    for i in matrix[99]:
        if i == 2:
            break
        x += 1

    return x

def start_x(matrix):
    row = 99
    col = direction_x(matrix)
    temp_col = col
    while row > 0:
        # print(row, col)
         # 왼쪽에서 오른쪽으로 움직였었다면.
        if temp_col == col -1 :

            if col+1 <100 and matrix[row][col+1]==1: # 조건을 이렇게 설정
                #하는 이유는 99번째 열에서 진행이 가능할 수도 있기 때문이다.
                 temp_col = col
                 col +=1
            elif matrix[row-1][col] == 1:
                 temp_col = col
                 row -= 1


        elif temp_col == col +1 :
            if 0<= col-1 and matrix[row][col-1] == 1:
                temp_col = col
                col -= 1
            elif matrix[row-1][col] ==1:
                temp_col =col
                row -=1
        else: #temp_col == col
            if col+1<100 and matrix[row][col+1] == 1:
                 col +=1

            elif 0<= col-1 and matrix[row][col - 1] == 1:
                 col -= 1
            elif matrix[row-1][col] == 1:
                 temp_col = col
                 row -= 1

    return col

T = 10
for _ in range(T):
    tc = int(input())
    matrix = [list(map(int, input().split())) for _ in range(100)]
    result = start_x(matrix)
    print(f'#{tc} {result}')

