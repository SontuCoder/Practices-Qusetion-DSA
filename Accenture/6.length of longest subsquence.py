# You are given on array of size N. You have to find the  
#  length of longest subsequence. In which every
# element is trice from previous.  

#IO: [2,3,6,18] ==> 3...[2,6,18]

def long(arr,current,prev):
    if(current==len(arr)):
        return 0

    pick=0
    if(prev==-1 or arr[current]==3*arr[prev]):
        pick = 1 + long(arr,current+1, current)

    no_pick=long(arr,current+1,prev)

    return max(pick, no_pick)

arr=[2,3,6,18]
print(long(arr,0,-1))

