# In: [3,1,4,5,6]
# Op: true, ....(3^2 + 4^2 = 5^2)

#In: [10,4,6,12,5]
#Op: False
#Time takes O(n*n)

# Marge Sort takes O(n*logn)
def marge(arr,low,mid,high):
    a=[]
    i=low
    k=low
    j=mid+1
    while(i<=mid and j<=high):
        if(arr[i]>=arr[j]):
            a.append(arr[j])
            k+=1
            j+=1
        else:
            a.append(arr[i])
            i+=1
            k+=1
    while(i<mid+1):
        a.append(arr[i])
        i+=1
        k+=1
    while(j<=high):
        a.append(arr[j])
        k+=1
        j+=1
    for i in range(low,high+1):
        arr[i]=a[i-low]

def margeSort(arr,low,high):
    if(low<high):
        mid=(low+high)//2
        margeSort(arr,low,mid)
        margeSort(arr,mid+1,high)
        marge(arr,low,mid,high)
    return arr

def triplet(arr):
    for i in range(len(arr)):
        arr[i]=arr[i]**2
    margeSort(arr,0,len(arr)-1)
    print(arr)
    for i in range(0,len(arr)-2):
        l=i+1
        r=len(arr)-1
        while(l<r):
            if(arr[i]==arr[r]-arr[l]):
                return True
            elif(arr[i]>arr[r]-arr[l]):
                l+=1
            else:
                r-=1
    return False


arr=[1,3,4,2,4,6,3,1]
print(triplet(arr))
