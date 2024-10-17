# LeetCode 121:

def max_profit(arr):
    min_price = 99999
    max_pro = 0
    for i in arr:
        min_price = min(min_price,i)
        profit = i-min_price
        max_pro = max(profit,max_pro)
    return max_pro


arr = [7,1,5,3,6,4]
print(max_profit(arr))