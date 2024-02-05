def solution(length, heights):
    count_heights = 0
    for i in range(2,length-2):
        max_height =0
        for j in range(i-2,i+3):
            if j == i:
                # pass 를 쓰게 되면 현재 j 와 i 가 같을 때 다음 구문인 8line을 실행한다. 그래서 max 값이 없게 된다. 
                continue
            if max_height <= heights[j]:
                max_height = heights[j]
        if heights[i] > max_height:
            count_heights += heights[i] - max_height
    return count_heights
T = 10
for t in range(T):
    N = int(input())
    a = list(map(int, input().split()))
    result = solution(N,a)
    print(f'#{t+1} {result}')
        

    