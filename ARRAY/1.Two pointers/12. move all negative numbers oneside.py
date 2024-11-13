# Move all the negative elements to one side of the array.

# Input: -12, 11, -13, -5, 6, -7, 5, -3, -6
# Output: -12 -13 -5 -7 -3 -6 11 6 5

def rearrange(arr):
    j = 0  
    for i in range(len(arr)):
        if arr[i] < 0:  
            arr[i], arr[j] = arr[j], arr[i]  
            j += 1 
    return arr

arr=[-12, 11, -13, -5, 6, -7, 5, -3, -6]
print(rearrange(arr))
