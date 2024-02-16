# #백만장자프로젝트
# def millionare(prices):
#     length = len(prices)
#     price_sum =0
#     for i in range(length-1):
#         max_value = max(prices[i+1:]) #이렇게 하면 매우 비효율적임 max 값을 매번 구해야함.

#         price = max_value - prices[i]
#         if price > 0:
#             price_sum += price
#
#     return price_sum
#
#
#
# T =int(input())
# for tc in range(1,T+1):
#     N = int(input())
#     numbers = list(map(int, input().split()))
#     result = millionare(numbers)
#     print(f'#{tc} {result}')
#

def millionare(prices):
    length = len(prices)
    max_price = prices[-1]
    profit = 0

    for i in range(length - 2, -1, -1):
        if prices[i] < max_price:
            profit += max_price - prices[i]
        else:
            max_price = prices[i]

    return profit


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    prices = list(map(int, input().split()))
    result = millionare(prices)
    print(f'#{tc} {result}')