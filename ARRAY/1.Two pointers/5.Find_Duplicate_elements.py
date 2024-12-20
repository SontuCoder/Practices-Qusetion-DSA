# find duplicate elements in O(n+m) time and O(1) space.
# Array contains elements from 0 to n-1.
#IO: [1,2,3,1,3,6,6] => [1,3,6]

def duplicate(arr):
    a=[0]*(max(arr)+1)
    for i in arr:
        a[i]+=1
    dup=[]
    for i in range(len(a)):
        if(a[i]>1):
            dup.append(i)
    return dup

arr=[1,2,3,1,3,6,9]
print(duplicate(arr))
