def GCD(lst):   #최대공약수를 구함으로써 비율 계산
    minimum = min(lst)
    length = len(lst)
    temp = 0
    for i in range(1,minimum+1):
        cnt = 0
        for sc in lst:
            if sc % i == 0:
                cnt += 1
        if cnt == length and temp < i:
            temp = i
    return temp

result = GCD([6,7,9])
print(result)