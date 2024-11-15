# Convert array into Zig-Zag fashion
# Given an array of distinct elements, rearrange the 
# elements of array in zig-zag fashion. The converted
# array should be in form a <b>c<d>e<f.

# Example:
# Input: arr[] = {4, 3, 7, 8, 6, 2, 1}
# Output: arr[] = {3, 7, 4, 8, 2, 6, 1}

# Input: arr[] = {1, 4, 3, 2}
# Output: arr[] = {1, 4, 2, 3}

def zig_zag(arr):
    flag = 1 # for "<"

    for i in range(len(arr)-1):
        if(flag): # for "<"
            if(arr[i]>arr[i+1]):
                arr[i], arr[i+1] = arr[i+1], arr[i]
        else: # for ">"
            if(arr[i]<arr[i+1]):
                arr[i], arr[i+1] = arr[i+1], arr[i]
        flag = not flag

arr= [4, 3, 7, 8, 6, 2, 1]
zig_zag(arr)
print(arr)