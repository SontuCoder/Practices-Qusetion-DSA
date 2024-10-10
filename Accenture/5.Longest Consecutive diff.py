# You are given on array of size N. You have to find the  
# length of longest subsequence. In which the difference
# of every consecutive element is divisible by k. 

# Inbut→ First having 2 integer contain N, K
# (Nis size of array), Next line integers representing array.

# single Integer. (length af longest subsequence)

#IO: [1,1,2,7,1], 3 ==> 6...[7,1] .. ([1,1] are also but diff(1,1) < diff(7,1))
#IO: [2,4],2  ==> 2....[2,4] 

# Method 1
def diff(arr,k):
    if(len(arr)<2):
        return "Invalid"
    max_diff=-99999
    for i in range(len(arr)-1):
        if(abs(arr[i]-arr[i+1])%k==0):
            max_diff=max(max_diff,abs(arr[i]-arr[i+1]))
    return max_diff



arr= [1,1,2,7,1]
k=3
print(diff(arr,k))