# First negative integer in every windoe of k

# Given an array A[] of size N and positive integer K,
# find the negative integer for each and every window of size K. 

# IO: [12,-1,-7,8,-15,30,16,28], k=3 => [-1,-1,-7,-15,-15,0]

# Method 1: 
def neg_int(arr,k):
    i=0
    li=[]
    while(i<=len(arr)-k):
        a = list(filter(lambda x : x <0, arr[i:i+k]))
        li.append(max(a) if len(a)>0 else 0)
        i+=1
    return li

arr = [12,-1,-7,8,6,4,-15,30,16,28]
k=3
print(neg_int(arr,k))