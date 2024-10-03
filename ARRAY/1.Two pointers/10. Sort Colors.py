# LeetCode: 75

# Array contains only 0,1,2 
# sort it in O(n) time
# IO: [2,0,1] ==> [0,1,2]
# IO: [2,0,2,1,1,0] ==> [0,0,1,1,2,2] 


def sort_Color(arr):
    l=0
    r=len(arr)-1
    curr=0
    while(curr<=r):
        if(arr[curr]==2):
            arr[r], arr[curr] = arr[curr], arr[r]
            r-=1
        elif(arr[curr]==1):
            curr+=1
        else:
            arr[l], arr[curr] = arr[curr], arr[l]
            l+=1
            curr+=1
    return arr


arr=[2,0,0,2,1,1,2]
print(sort_Color(arr))

