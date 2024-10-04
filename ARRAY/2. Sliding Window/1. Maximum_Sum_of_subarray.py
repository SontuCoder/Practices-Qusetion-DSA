# Max sum of sum array of size k

#IO: [2,5,1,-8,2,9,1], size= 3 ..==> 12..(2,9,1)
#IO: [4,56,-7,3,-1,1,4,6,-3,2,54], size = 5.. ==> 63..(4,6,-3,2,54)

# takes O(n)
def max_sum_array(arr,n):
    sum=0
    for i in range(n):
        sum += arr[i]
    max_sum=sum
    for i in range(n,len(arr)):
        sum=sum-arr[i-n]+arr[i]
        max_sum=max(max_sum,sum)
    return max_sum

arr= [4,56,-7,3,-1,1,4,6,-3,2,54]
n=5
print(max_sum_array(arr,n))
