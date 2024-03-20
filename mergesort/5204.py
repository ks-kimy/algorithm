import sys
sys.stdin = open("input.txt", "r")

def merge_sort(arr):
    global cnt
    if len(arr) < 2:
        return arr
    mid = len(arr) // 2

    left_arr = merge_sort(arr[:mid])
    right_arr = merge_sort(arr[mid:])
    if left_arr[-1] > right_arr[-1]:
        cnt +=1
    return merge(left_arr, right_arr)
# return merge 가 나오면 밑의 merge 함수로 가서 merge 함수가 실행되고
# 마지막 return merge_arr 이 실행되며   left_arr = merge_sort(arr[:mid]) 이 값에 left_arr 에 merge_arr가 들어감.
# 그런데 list 는 정보가 기억되지 않느냐 라고 질문할 수 있겠지만. 재귀함수의 특징은 그 시점에서의 값은 다르다는 것이다. 
# 따라서 merge_arr 와 left_arr, right_arr 가 계속해서 갱신된다. 

def merge(left_arr, right_arr):

    merge_arr = []
    len_l = len(left_arr)
    len_r = len(right_arr)
    len_m = len_l + len_r
    i = j = 0
    while len(merge_arr) < len_m:
        if i == len_l:
            merge_arr.append(right_arr[j])
            j+=1
            continue
        if j == len_r:
            merge_arr.append(left_arr[i])
            i+=1
            continue

        if left_arr[i] <= right_arr[j] :
            merge_arr.append(left_arr[i])
            i += 1
            continue
        if left_arr[i] > right_arr[j]:
            merge_arr.append(right_arr[j])
            j += 1
            continue
    return merge_arr


T= int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    print(f'#{tc}', end=' ')
    print(merge_sort(arr)[N//2], end=' ')
    print(cnt)
