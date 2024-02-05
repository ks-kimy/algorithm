N = int(input())
arr = list(map(int, input().split()))

max_v = 0
for i in range(N-1):
    cnt = 0  #오른쪽에 있는 더 낮은 높이의 갯수.
    for j in range(i+1, N):
        if arr[i] > arr[j]:
            cnt += 1
    if max_v < cnt:
        max_v = cnt
print(max_v)


