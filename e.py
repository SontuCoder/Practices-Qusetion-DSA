
def sort_2nd(arr):
    ind=arr.index(max(arr))
    max_2nd=arr[0]
    for i in range(1,len(arr)):
        if((max_2nd < arr[i]) and i != ind):
            max_2nd = arr[i]
    return max_2nd


arr=[1,3,53,2,4,6,5,3,2,]
print(sort_2nd(arr))
