# Move all the negative elements to one side of the array.

# Input: -12, 11, -13, -5, 6, -7, 5, -3, -6
# Output: -12 -13 -5 -7 -3 -6 11 6 5

def move(arr):
    i=len(arr)-1
    j=len(arr)-1
    while(j>=0):
        if(arr[i]>=0 and arr[j]>=0):
            i-=1
            j=i
        elif(arr[i]<0 and arr[j]>=0):
            arr[i], arr[j] = arr[j], arr[i]
            i-=1
            j-=1
        elif(arr[j]<0):
            j-=1
        print(arr)

arr=[-12, 11, -13, -5, 6, -7, 5, -3, -6]
move(arr)
