# #문자열 비교
#
# T = int(input())
# for tc in range(T):
#     lst1 = list(input())
#     lst2 = list(input())
#     length1 = len(lst1)
#     length2 = len(lst2)
#     for j in range(length2-length1+1):
#         temp = 0
#         if lst1[0]== lst2[j]:
#             for i in range(length1):
#                 if lst1[i] == lst2[j+i]:
#                     temp =1
#                 else:
#                     temp = 0
#                     break
#         if temp ==1:
#             print(f'#{tc+1} 1')
#             break
#         elif j == length2 -length1 and temp ==0:
#             print(f'#{tc+1} 0')
#
#
#
#




T = int(input())
for tc in range(1, T+1):
    str1, str2 = [input() for _ in range(2)]
    print(f'#{tc} {int(str1 in str2)}')
