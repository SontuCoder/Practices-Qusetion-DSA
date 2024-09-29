# IO:- [16,17,4,3,5,2]
# OP:- [17,5,5,5,2,-1]
# last element replace with -1

def repla(arr):
    if(len(arr)==0):
        return arr
    greatest=arr[len(arr)-1]
    arr[len(arr)-1]=-1
    for i in range(len(arr)-2,-1,-1):
        now=arr[i]
        arr[i]=greatest
        if(greatest<now):
            greatest=now
    return arr



arr=[1,18,17,4,7,5,2]

print(repla(arr))