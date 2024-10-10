#  Superior Array elements:
#  In an array a superior element is one which is greater than all elements to its right.

# In1: [16,17,4,3,5,2]
# out1: [17,5,2]


def super(arr):
    maximum=arr[-1]
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
print(super(arr))