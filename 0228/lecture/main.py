arr = ['A','B', 'C','D','E','F','G','H','I','J']
n = len(arr)

def get_sub(tar):
    for i in range(n):
        if tar & 1:
            print(arr[i], end='')
        tar >>= 1

for tar in range(1 << n):
    print('{', end='')
    get_sub(tar)
    print('}')