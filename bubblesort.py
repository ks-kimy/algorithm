N = 6
arr = [7, 2, 5, 3, 1, 4]
for i in range(N-1, 0, -1):
    for j in range(i):
        if arr[j] > arr[j+1]: #오름차순은 큰 수를 오른쪽으로
            arr[j], arr[j+1] = arr[j+1], arr[j]
print(arr)