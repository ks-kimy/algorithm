N = 3
arr = [1,2,3]

for i in range(1<<N):
    for j in range(N):
        if i & (1<<j): #j 번째 비트가 1이고 나머지 비트는 0이다.
# i 가 3일 때 011 이다. 이것은 arr 배열의 첫번째 두번째 원소가 포함된다는 뜻.
# 그렇기에 j를 N번 0,1,2 하면서 011 과 001, 010, 100  이것들을 각각
# 비트 연산으로 참인지 아닌지 구별.
# 예를 들어 011과 001 은 참이기 때문에 0번째 원소 arr[0] => 1 을 출력.
            print(arr[j], end= ' ')
    print()
#
# print(0<<0)