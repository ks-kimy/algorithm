#초심자의 회문 검사
def reverse_words(arr):
    length = len(arr)
    lst = list(arr)
    for i in range(length // 2):
        lst[i], lst[length - 1 - i] = lst[length - 1 - i], lst[i]
    result = ''.join(lst)
    return result



T = int(input())
for tc in range(T):
    arr =  input()
    arr2 = reverse_words(arr)
    if arr == arr2:
        temp = 1
    else:
        temp = 0

    print(f'#{tc+1} {temp}')