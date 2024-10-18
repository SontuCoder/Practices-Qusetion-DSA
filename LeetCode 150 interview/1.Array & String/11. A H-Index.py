# leet code: 275 
# H-Index II


# Method 1 : takes O(logn)
def h_index(arr,low,n):
    high=n-1
    while(low<=high):
        mid=(low+high)//2
        if(arr[mid]==len(arr)-mid):
            return arr[mid]
        elif(arr[mid]>len(arr)-mid):
            high=mid-1
        else:
            low=mid+1
    print(n,low)
    return n-low


arr=[1,6,6,7,8]
print(h_index(arr,0,len(arr)))