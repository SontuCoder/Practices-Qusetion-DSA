# Leet Code: 274

# method 1: takes O(n*logn)
def h_index(arr,low,n):
    arr.sort()
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


arr=[3,0,1,6,6,8]
print(h_index(arr,0,len(arr)))