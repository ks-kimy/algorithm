N =5
arr = [[0]*N for _ in range(N)]

for i in range(N):
    for j in range(N):
        print(arr[i][j], end=' ')
    print()

print()

arr2 = [list(range(i*N,(i+1)*N)) for i in range(N)]
# 0N ~ 1N
# 1N ~ 2N
# ....

for i in range(N):
    for j in range(N):
        print(arr2[i][j], end=' ')
    print()

print()

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
# 오른쪽, 아래, 왼쪽, 위
for i in range(N):
    for j in range(N):
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0<=ni<N and 0<=nj<N:
                print(arr2[ni][nj], end=' ')
        print()