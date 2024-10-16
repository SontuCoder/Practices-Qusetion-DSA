# Leetcode: 26

def duplicate(arr):
    pre=arr[0]
    count=1
    for i in range(1,len(arr)):
        if(arr[i]!=pre):
            pre=arr[i]
            count+=1
    return count

arr=[1,1,1,2,3,3]

print(duplicate(arr))

