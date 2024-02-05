#부분집합의 합
def my_len(sample_list):
    num = 0
    for lst in sample_list:
        num += 1
    return num

def my_sum(sample_list):
    temp = 0
    for lst in sample_list:
        temp += lst
    return temp


A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
T = int(input())
for t in range(T):
    N, K = map(int, input().split())
    print(N)