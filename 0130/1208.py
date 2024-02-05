def my_len(sample_list):
    num = 0
    for sample in sample_list:
         num += 1
    return num

def my_max(length,sample_list):
    temp = sample_list[0]
    temp_leng = 0
    for leng in range(length):
        if sample_list[leng] > temp:
            temp = sample_list[leng]
            temp_leng = leng
    return temp, temp_leng

def my_min(length, sample_list):
    temp = sample_list[0]
    temp_leng = 0
    for leng in range(length):
            if sample_list[leng] < temp:
                temp = sample_list[leng]
                temp_leng = leng
    return temp, temp_leng

def dumping(dumps, heights):
    length = my_len(heights)
    for dump in dumps:
        max_num, max_index = my_max(length, heights)
        min_num, min_index = my_min(length, heights)
        heights[max_index] -= 1
        heights[min_index] += 1
        if dump == dumps:
            result =  heights[max_index] - heights[min_index]
    return result 
        

T = 10

for t in range(T):
    dumps = int(input())
    heights = list(map(int, input().split()))
    result = dumping(dumps, heights)
    print(f'#{t+1} {result}')