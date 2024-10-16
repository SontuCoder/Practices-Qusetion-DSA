#Leetcode 189

# method 1: takes O(n^k) time
def rotate(arr):
    a=arr[len(arr)-1]
    for i in range(len(arr)-2,-1,-1):
        arr[i+1]=arr[i]
    arr[0]=a

def arr_rotate(arr,k):
    for i in range(k):
        rotate(arr)
    return arr

# Method 2 : O(n) time and O(1) space
def rotate_arr(arr,k):
    li=[]
    for i in range(len(arr)-k,len(arr)):
        li.append(arr[i])
    for i in range(0,len(arr)-k):
        li.append(arr[i])
    return li


arr=[1,2,3,4,5,6,7]
print(rotate_arr(arr,3))