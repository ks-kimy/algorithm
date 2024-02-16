#파스칼의 삼각형
def pascal(size):
    temp_matrix =[]
    for i in range(size):
        temp_lst = []
        for j in range(i+1):
            if (i-1)>=0 and (j-1)>=0 and j<=i-1: # j<=i-1 이여야함. 왜냐하면 전 row에서의 값들을 받아오는 것이기 때문
                # 밑에 넘버는 i 가 업데이트 되고나서의 i 이기 때문에.
                number = temp_matrix[i-1][j-1] + temp_matrix[i-1][j]
                temp_lst.append(number)
            else:
                temp_lst.append(1)
        temp_matrix.append(temp_lst)
    return temp_matrix

T = int(input())

for tc in range(T):
    size = int(input())
    result = pascal(size)
    print(f'#{tc+1}')
    # print(result)
    for i in range(size):


        # result2 = ' '.join(map(str, result[i]))
        print(*result[i])
