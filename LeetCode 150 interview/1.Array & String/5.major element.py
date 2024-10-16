#Leetcode 169

def major(arr):
    j=1
    prev=arr[0]
    for i in range(1,len(arr)):
        if(arr[i]==prev):
            j+=1
        else:
            if(j==0):
                prev=arr[i]
                j=1
            else:
                j-=1
    return prev

arr=[2,2,1,1,1,2,2]
print(major(arr))




