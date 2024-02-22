# 이진수
# import sys
# sys.stdin = open("20240.txt", "r")
# sys.stdout = open("20240_out.txt", "W")
def binary(word):
    if word.isalpha():
        if word == 'A':
            return '1010'
        elif word == 'B':
            return '1011'
        elif word == 'C':
            return '1100'
        elif word == 'D':
            return '1101'
        elif word == 'E':
            return '1110'
        elif word == 'F':
            return '1111'
    else:
        temp_arr = [0]*4
        number = int(word)
        i =0
        empty= ''
        while number != 0:
            rest = number % 2
            number //= 2
            temp_arr[i] = rest
            i+=1

        temp_arr.reverse()


        for i in range(4):
            empty += str(temp_arr[i])

        return empty
T = int(input())
for tc in range(1, T+1):

    N, arr = input().split() #
    N = int(N)
    result_arr = ''
    for i in range(N):
        result_arr += binary(arr[i])

    print(f'#{tc} {result_arr}')
