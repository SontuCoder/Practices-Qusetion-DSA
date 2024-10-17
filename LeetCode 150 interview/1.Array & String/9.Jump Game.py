# Leetcode 55

def jump(arr):
    reach_index=0
    for i in range(len(arr)):
        if(reach_index<i):
            return False
        reach_index=max(reach_index,i+arr[i])
    return True

arr=[2,2,2,0,4]
print(jump(arr))
