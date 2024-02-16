def sdocu(matrix):
    numbers = [i for i in range(1,10)]
    right =0
    down = 0
    nine = 0
    for i in range(9):
        lst1 = list(matrix[i][k] for k in range(9))
        lst1.sort()
        if numbers == lst1:
            right =1
        else:
            right = 0
            break
    for j in range(9):
        lst2 = list(matrix[k][j] for k in range(9))
        lst2.sort()
        if numbers == lst2:
            down =1
        else:
            down = 0
            break

    #9개의 영역 구하기
    temp = []
    for i in range(0,9,3):
        for j in range(0,9,3):
            temp_matrix = [row[j:j+3] for row in matrix[i:i+3]]
            temp.append(temp_matrix)

    for i in range(9):
        check_9 = []
        for j in range(3):
            for k in range(3):
                check_9.append(temp[i][j][k])
        check_9.sort()
        if numbers == check_9:
            nine =1
        else:
            nine =0
            break



    if right ==1 and down ==1 and nine ==1:
        return 1
    else:
        return 0

T= int(input())

for tc in range(1,T+1):
    matrix = [list(map(int, input().split())) for _ in range(9)]
    result = sdocu(matrix)
    # print(result[0][1][2])
    print(f'#{tc} {result}')