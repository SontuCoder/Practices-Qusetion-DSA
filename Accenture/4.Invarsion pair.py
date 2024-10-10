# Inversion pair: 
# if i<j and arr[i] > arr[j], then [i,j] is called Innversion pair.
# if len(arr)==0, return -1
# if len(arr)<2, return 0
# otherwise return number of pair.
# IO: [1,20,6,4,5] ==> 5

def inver_pair(arr):
    if(len(arr)==0):
        return -1
    if(len(arr)==1):
        return 0
    li=0
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            if((i<j) and (arr[i] > arr[j])):
                li+=1
    return li

arr=[]
print(inver_pair(arr))