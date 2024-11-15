# Note: Array is sort according 1D
# [[1,2,3],[4,5,6],[7,8,9]] => [1,2,3,4,5,6,7,8,9]

def Binary_Search(arr,element):
    row = len(arr)
    column = len(arr[0])
    start=0
    end = row*column-1
    mid = start+(end-start)//2
    while(start<=end):
        mid = start+(end-start)//2
        if(arr[mid//column][mid%column]>element):
            end=mid-1
        elif(arr[mid//column][mid%column]<element):
            start = mid+1
        else:
            return "Found" 
    return "Not Found"

arr = [[1,2,3],[4,5,6],[7,8,9]]
print(Binary_Search(arr,9))
