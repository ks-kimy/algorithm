#GNS
words= ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
def changing_num(word):
    for i in range(10):
        if word == words[i]:
            changed_num = i
    return changed_num

    #외계인 녀석들의 숫자를 인간의 숫자체계로 변화.

def gns(arr):
    empty_arr =[0]*length
    counting_arr = [0]*10
    for i in range(10):
        for j in range(length):
            if words[i] == arr[j]:
                counting_arr[i] += 1

    for i in range(1, 10):
        counting_arr[i] += counting_arr[i-1]

    for i in range(length-1,-1,-1):
        counting_arr[changing_num(arr[i])] -= 1
        empty_arr[counting_arr[changing_num(arr[i])]] = arr[i]

    return empty_arr
    #카운팅정렬을 통해 구현.
T = int(input())
for tc in range(T):
    input_sample = input().split()
    testcase = input_sample[0]
    length = int(input_sample[1])
    arr = input().split()
    result = gns(arr)
    result2 = ' '.join(result)
    print(testcase)
    print(result2)
