#Leetcode:- 26, 80
# Array is sorted:
#IO: [0,1,1,2,2,2,2,3] ==> [0,1,2,3]

#Method 1:
def removeDuplicates(nums):
    n=len(nums)-1
    j=0
    while(j<n):
        if(nums[j]==nums[j+1]):
            nums.pop(j)
            n-=1
        else:
            j+=1
    return nums

# Method 2: By Two Pointers
def removeDupli(arr):
    i=0
    j=i+1
    while(j<len(arr)):
        if(arr[i]==arr[j]):
            j+=1
        else:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
            j+=1
    return arr[0:i+1]



arr=[0,1,1,2,2,2,2,3]
print(removeDuplicates(arr))
print(removeDupli(arr))