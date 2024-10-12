# Some as superior element,

# You are on a hiking trail represented by an Array A of length N.
# Where the trial initially ascends and then descends forming a single peek.
# Your task is to find and return an integer value representing the elevation of the summit.

# Ip: N=7, Arr = [1,2,3,4,3,2,1] ==> 4
# IP: N=2, Arr = [5,3] ==> 5

def peek_point(arr,low,high):
    if low == high:
        return arr[low]
    
    mid = (low + high) // 2
    
    if arr[mid] > arr[mid + 1] and arr[mid] > arr[mid - 1]:
        return arr[mid]
    elif arr[mid] < arr[mid + 1]:
        return peek_point(arr, mid + 1, high)
    else:
        return peek_point(arr, low, mid - 1)


arr=[1,2,3,5,3,2,1]
print(peek_point(arr,0,len(arr)-1))
