# In1: [16,17,4,3,5,2]
#out1: [17,5,2]

# Leader element: whose value is greater than of all its right values.

def lead(arr):
    maximum=arr[len(arr)-1]
    leader=[maximum]
    for i in range(len(arr)-2,0,-1):
        if(arr[i]>maximum):
            maximum=arr[i]
            leader.insert(0,maximum)
    return leader



n = int(input("Enter the number of element: "))
arr=[0]*n
for i in range(n):
    arr[i]= int(input(f"enter the number in {i}: "))
print("Array:-")
print(arr)
print("The leading elements:-")
print(lead(arr))
