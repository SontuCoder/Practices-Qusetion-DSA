# Leetcode:- 135

def candy(ratings):
    n = len(ratings)
    
    # Step 1: Assign 1 candy to each child initially
    candies = [1] * n
    
    # Step 2: Traverse from left to right
    for i in range(1, n):
        if ratings[i] > ratings[i - 1]:
            candies[i] = candies[i - 1] + 1
    
    # Step 3: Traverse from right to left
    for i in range(n - 2, -1, -1):
        if ratings[i] > ratings[i + 1]:
            candies[i] = max(candies[i], candies[i + 1] + 1)
    
    # Step 4: Return the total number of candies
    return sum(candies)



arr=[1,3,2,2,1]
print(candy(arr))