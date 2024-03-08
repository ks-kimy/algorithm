import sys
sys.stdin = open("input.txt", "r")
# 방향에 따른 이동방향.
def vector(row, col, vec):
    if vec ==1:
        return row - 1, col
    if vec ==2:
        return row + 1, col
            
    if vec ==3:
        return row, col - 1
            
    if vec ==4:
        return row, col + 1
    
#방향이 변함을 구하는 함수.
def vector_change(vec):
    if vec == 1:
        return 2
    if vec == 2:
        return 1
    if vec == 3:
        return 4
    if vec == 4:
        return 3

def killing_micro(row,col,nums,vec):
    if row == 0 or col == 0 or row == N-1 or col == N-1 :
        nums //= 2 
        vec = vector_change(vec)
    
    return nums, vec

    
def result_arr(arg):
    index =0
    while True:
        if index == len(microorg)-1:
            return
        temp = index   
        row = microorg[index][0]
        col = microorg[index][1]
        nums = microorg[index][2]
        vec = microorg[index][3]
        # if nums == 0 :
        #     microorg.pop(index)
        # 야 이거 뭔데!!!! 이게 지우니까 왜 되는데!!
        #
        # 아 여기서 만약 팝이 되어 버리면 만약 모두 1의 미생물의 갯수를 가진것들이 있다고 보자. 그러면 몇 개의 것들은 1회가 지나면 바로 0이 되어버린다. 
        #거기서 팝을 때려버리면 인덱스가 비게 되고 다음 while 문의 index 에서 에러가 #떠버린다. 
        #
        #
        #
        while True:
            index += 1
            if microorg[index][0] == row and microorg[index][1] == col:
                microorg[temp][2]  += microorg[index][2]
                microorg[index][2] = 0
                microorg.pop(index)
                index -= 1
            else:
                break
            if index == len(microorg)-1:
                return
        
        
       

T = int(input())
for tc in range(1, T+1):
    N,M,K = map(int,input().split())
    result = 0
    microorg = [list(map(int,input().split())) for _ in range(K)]
    while M>0:
        M -= 1
        for i in range(len(microorg)):
            row = microorg[i][0]
            col = microorg[i][1]
            nums = microorg[i][2]
            vec = microorg[i][3]

            row, col  = vector(row,col,vec)
            nums, vec = killing_micro(row,col,nums,vec)
            microorg[i][0] = row
            microorg[i][1] = col
            microorg[i][2] = nums
            microorg[i][3] = vec
        microorg.sort(key= lambda x : (x[0], x[1],x[2]), reverse=True)

        result_arr(microorg)

    # print(microorg)
    for i in range(len(microorg)):
        result += microorg[i][2]
        # print(result)
    print(f'#{tc} {result}')

   
