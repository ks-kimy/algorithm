#이진탐색
def binary(end_pages,find_pages):
    start_page = 1
    cnt = 0
    while start_page <= end_pages:
        middle_pages= (start_page+end_pages)//2
        if middle_pages < find_pages:
            start_page = middle_pages
            cnt += 1
        elif middle_pages > find_pages:
            end_pages = middle_pages
            cnt += 1
        else: #middle_pages == find_pages
            return cnt





T = int(input())
for tc in range(T):

    P , Pa, Pb = map(int, input().split())
    # print(P,Pa,Pb)
    result = binary(P,Pa)

    result2 = binary(P, Pb)

    if result > result2:
        print(f'#{tc+1} B')
    elif result < result2:
        print(f'#{tc+1} A')
    else:
        print(f'#{tc+1} 0')
