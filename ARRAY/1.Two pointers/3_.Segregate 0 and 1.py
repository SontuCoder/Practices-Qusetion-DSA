#Leetcode:- 283
#IO: [1,0,0,1,1,0] => [0,0,0,1,1,1]

# Method 1: Sorting take O(n^2) or O(n^logn)
# Method 2: Count 0 or 1 , takes O(n) time
# Method 3: By Two poins Algo takes O(n) time


# Method 3:

def segregate(arr):
    i=0
    j=len(arr)-1
    while(i<j):
        if(arr[i]==0):
            i+=1
        elif(arr[j]==1):
            j-=1
        else:
            arr[i],arr[j]=arr[j],arr[i]
            i+=1
            j-=1
    return arr

arr=[1,0,0,1,1,0,1,1,0]
print(segregate(arr))