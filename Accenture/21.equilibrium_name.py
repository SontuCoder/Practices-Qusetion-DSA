# The function accepts an integer array 'arr' of size 'n' as its 
# argument. The function needs to return the index of an equilibrium 
# point in the array, where the sum of elements on the left of the 
# index is equal to the sum of elements on the right of the index. 
# If no equilibrium point exists return -1.

# IO: [-7,1,5,2,-4,3,0] ==> 3 ..(arr[3]==2)
# note: prefix sum of index 2:  -7+1+5 = -1
#       sufix sum of index 2: 5+2-4+3+0 = 6

def equilibrium(arr):
    sufix=[0]*(len(arr))
    prefix=[0]*(len(arr))

    prefix_sum=0
    for i in range(len(arr)):
        prefix_sum+=arr[i]
        prefix[i]=prefix_sum
    sufix_sum=0
    for i in range(len(arr)-1,0,-1):
        sufix_sum+=arr[i]
        sufix[i]=sufix_sum
    for i in range(len(arr)):
        if(sufix[i]==prefix[i]):
            return i
    return -1

arr=[-7,1,-5,-2,-4,3,0]
print(equilibrium(arr))