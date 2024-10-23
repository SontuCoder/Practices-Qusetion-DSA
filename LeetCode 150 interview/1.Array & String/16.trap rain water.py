# Leetcode 42:-

def water(arr):
    max_height = arr.index(max(arr))
    total_water= 0
    left_max=0
    for i in range(max_height):
        if(arr[i]>arr[left_max]):
            left_max=i
        else:
            total_water+=(arr[left_max]-arr[i])
    right_max=len(arr)-1
    for i in range(len(arr)-1,max_height,-1):
        if(arr[i]>arr[right_max]):
            right_max=i
        else:
            total_water+=(arr[right_max]-arr[i])
    print(total_water)



arr = [4,2,3]
water(arr)