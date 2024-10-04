# IO:- [3,4,5,1,2]  ==> Pivot point is only element for 
#                       which next element to it is smaller 
#                       than it. (like 5)

# binary search
def binary(arr, low, high, x):
    # An iterative binary search function.
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == x:
            return mid
        if arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def findpivot(arr, low, high):
    while low < high:
        if arr[low] <= arr[high]:
            return low
        
        mid = (low + high) // 2
        if arr[mid] > arr[high]:
            low = mid + 1
        else:
            high = mid
    return low


def pivotSearch(arr, key):
    #Searches an element key in a pivoted sorted array arr of size n 
    pivot = findpivot(arr, 0, len(arr) - 1)

    # If the minimum element is present at index 0, then the whole array is sorted
    if pivot == 0:
        return binary(arr, 0, len(arr) - 1, key)

    # If we found a pivot, then first compare with pivot and then search in two subarrays around pivot
    if arr[pivot] == key:
        return pivot

    if arr[0] <= key:
        return binary(arr, 0, pivot - 1, key)
    return binary(arr, pivot + 1, len(arr) - 1, key)

arr=[3,4,5,1,2]
if(pivotSearch(arr,1)==-1):
    print("element is not in array.")
else:
    print(f"element index is {pivotSearch(arr,1)}")