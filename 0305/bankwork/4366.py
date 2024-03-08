import sys
sys.stdin = open("input.txt", "r")
def change_bin(num):
    if num == 1:
        return 0
    if num == 0:
        return 1
def check_same(bin_arr, thd_arr):
    num1 = int(''.join(map(str, bin_arr)),2)   
    num2 = int(''.join(map(str,thd_arr )),3)
    if num1 == num2 :
        return num1
    
def bank():
    for b_i in range(b_len-1,-1,-1):
        binary[b_i] = change_bin(binary[b_i])
        for t_i in range(t_len-1,-1,-1):
            save = third[t_i]
            for i in range(3):
                if third[t_i] == i:
                    continue
                third[t_i] = i
                if check_same(binary,third):
                    return check_same(binary, third)
                else:
                    third[t_i] = save
        binary[b_i] = change_bin(binary[b_i])
        




T= int(input())
for tc in range(1, T+1):
    binary = list(map(int, input()))
    b_len = len(binary)
    third = list(map(int, input()))
    t_len = len(third)
    result = bank()
    print(f'#{tc} {result}')
