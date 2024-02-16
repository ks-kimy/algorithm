#반복문자 지우기
def erase(arr):
    temp_arr = []
    length = len(arr)
    for word in arr:
        temp_arr.append(word)
        length2 = len(temp_arr)
        if length2>=2 and temp_arr[length2-1] ==temp_arr[length2-2]:
            temp_arr.pop()
            temp_arr.pop()
    final_length = len(temp_arr)
    return final_length




T = int(input())

for tc in range(1,T+1):
    arr = input()
    result = erase(arr)
    print(f'#{tc} {result}')