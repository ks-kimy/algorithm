# #특별한 정렬
def special_sort(length,arr):
    temp_arr = [0]*length
    for i in range(length,length//2,-1):
        temp_arr[(length-i)*2] = arr[i-1]
    for i in range(0,length//2):
        temp_arr[i*2+1] = arr[i]

    return temp_arr

def ten_arr(arr):
    temp_arr = [0]*10
    for i in range(10):
        temp_arr[i]=arr[i]

    return temp_arr
#
#
T = int(input())
for tc in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    result = special_sort(N,arr)
    result2 = ten_arr(result)
    print(f'#{tc+1}', *result2)
# arr= list(range(7,7//2,-1))
# print(arr)
# arr2 = list(range(1,10))
# print(arr2)