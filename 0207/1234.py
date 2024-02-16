#비밀번호
def password(arr):
    temp_arr = []
    for i in arr:
        temp_arr.append(i)
        length = len(temp_arr)
        if length >=2 and temp_arr[length-2] ==temp_arr[length-1]:
            temp_arr.pop()
            temp_arr.pop()

    return temp_arr
# [12342124]
T = 10

for tc in range(T):
    N, arr = input().split()
    arr = list(map(int,arr)) # [arr]
    result = password(arr)
    print(f'#{tc+1} ', *result,sep='')
