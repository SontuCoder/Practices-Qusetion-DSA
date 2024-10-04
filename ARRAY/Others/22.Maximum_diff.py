# Maximun different between two elements such 
# that larger element appears after the smaller.

# IO: [2,3,10,6,4,8,1] => 8 ..(2,10)
# IO: [7,9,5,6,3,2] => 2 ..(7,9)

def max_difference(arr):  # Takes O(n) time
    max_diff=arr[1]-arr[0]
    min_element=arr[0]
    for i in range(1,len(arr)):
        if(arr[i]-min_element>max_diff):
            max_diff=arr[i]-min_element
        if(min_element>arr[i]):
            min_element=arr[i]
    return max_diff

# Method 2 Using Kadanse's algo

def max_difference2(arr):
    a=[]
    for i in range(1,len(arr)):
        a.append(arr[i]-arr[i-1])
    curr=a[0]
    for i in range(1,len(a)):
        if(a[i-1]>0):
            a[i]+=a[i-1]
        if(curr<a[i]):
            curr=a[i]
    return curr

arr=[2,3,10,6,4,11,1] 
print(max_difference2(arr))