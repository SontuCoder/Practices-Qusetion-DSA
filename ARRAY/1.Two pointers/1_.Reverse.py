def reverse(arr):
    i=0
    j=len(arr)-1
    while(i<j):
        arr[i],arr[j]=arr[j],arr[i]
        i+=1
        j-=1
    return arr

def rever(arr):
    return arr[::-1]

arr=[74,5,3,2,7,3,2]
print(rever(arr))