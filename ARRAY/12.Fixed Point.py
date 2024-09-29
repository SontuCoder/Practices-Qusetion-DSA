# which element value= index is called fixed element.
#IO:- [1,2,4,3,5]
# OP:- 3=arr[3]
# if array has no fixed then return -1

def fixed(arr):
    for i in range(len(arr)):
        if(arr[i]==i):
            return i
    return -1

arr= [1,2,4,3,5]
print(fixed(arr))