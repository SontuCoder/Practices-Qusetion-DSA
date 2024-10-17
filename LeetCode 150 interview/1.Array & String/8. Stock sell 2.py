# LeetCode 122:


def profit_func(prices):
    profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            profit += prices[i] - prices[i - 1]
    return profit

arr = [6,1,3,2,4,7]
print(profit_func(arr))