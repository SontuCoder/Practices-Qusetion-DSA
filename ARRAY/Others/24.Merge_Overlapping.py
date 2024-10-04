# IO: [[1,3],[2,4],[5,7],[6,8]] => [[1,4],[5,8]]

def marge(arr,low,mid,high):
    a=[]
    i=low
    k=low
    j=mid+1
    while(i<=mid and j<=high):
        if(arr[i][0]>arr[j][0]):
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

def merge_overlaps(arr):
    margeSort(arr,0,len(arr)-1)  # sort array of arrays in accending order according the starting point of every interval.
    a=[]
    a.append(arr[0])
    for i in range(1,len(arr)):
        top=a[len(a)-1]
        if(top[1]<arr[i][0]):
            a.append(arr[i])
        elif(top[1]<arr[i][1]):
            top[1]=arr[i][1]
            a.pop()
            a.append(top)
    return a


arr=[[1,3],[5,7],[6,8],[2,4],[9,10]]
print(merge_overlaps(arr))