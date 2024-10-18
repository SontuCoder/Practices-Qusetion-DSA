
def sort_2nd(arr):
    for i in range(len(arr)-1,-1,-1):
        if(arr[i]-1==(len(arr)-1-i)):
            return arr[i]
    return -1

arr=[0,1,3,5,6]
print(sort_2nd(arr))
