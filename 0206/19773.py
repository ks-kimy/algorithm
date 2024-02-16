#글자수

T = int(input())
for tc in range(1,T+1):
    str1 = input()
    str2 = input()
    count_list =[]
    str1_len = len(str1)
    str2_len = len(str2)
    lst_str1 = list(str1)
    for i in range(str1_len):
        cnt = str2.count(lst_str1[i])
        count_list.append(cnt)

    max_num = max(count_list)
    print(f'#{tc} {max_num}')