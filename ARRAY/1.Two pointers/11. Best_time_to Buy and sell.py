# Best time to buy stock and sell:

#IO: [7,1,5,3,6,4] ==> 5 ..(6-1)

# Method 1:  O(n)
def buy_sell(arr):
    i=0
    j=1
    max_profit=0
    while(j<len(arr)):
        if(arr[i]<arr[j]):
            profit=arr[j]-arr[i]
            max_profit=max(max_profit, profit)
        else:
            i+=1
        j+=1
    return max_profit

arr= [1,7,1,5,3,6,4]
print(buy_sell(arr))

