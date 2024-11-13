# Leetcode: 42 (Hard)

#IO: [0,1,0,2,1,0,1,3,2,1,2,1] ==> 6 units
#IO: [4,2,0,3,2,5] ==> 9 units
#IO: [4,2,3] ==> 1 unit

# main concept (Hint) -> water in curent position
# = Min height( left max height, right max height) - current height

#Process:
# 1. find max height index
# 2. count water from left and also take max left height
# 3. cunnt water from right and also take max right height

# Method 1. takes O(n) and space O(n)
def water(arr):  
    max_height = 0
    for i in  range(len(arr)):
        if(arr[i]> arr[max_height]):
            max_height=i
    sum_water = 0
    left_max = 0
    for i in range(max_height):
        if(arr[left_max]<arr[i]):
            left_max = i
        sum_water += arr[left_max] - arr[i]
        
    right_max = len(arr)-1
    for i in range(len(arr)-1,max_height,-1):
        if(arr[right_max]<arr[i]):
            right_max = i
        sum_water += arr[right_max] - arr[i]
    return sum_water

arr = [0,1,0,2,1,0,1,3,2,1,2,1]
print(water(arr))