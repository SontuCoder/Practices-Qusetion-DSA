# IO: [1,5,3,19,18,25] => 1.. (19-18)
#IO: [30,5,20,9]  => 4.. (5-9)
#IO: [1,19,-4,31,38,25,100] => 5.. (1--4)

# Method 1 takes O(n^2)
def dist(arr):
    min_dist= 99999999
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            if(abs(arr[i]-arr[j])<min_dist):
                min_dist=abs(arr[i]-arr[j])
    return min_dist

# Method 2 takes O(n*logn)

def marged(arr,low,mid,high):
    i=low
    j=mid+1
    a=[]
    while(i<mid+1 and j<high+1):
        if(arr[i]>=arr[j]):
            a.append(arr[j])
            j+=1
        else:
            a.append(arr[i])
            i+=1
    while(i<mid+1):
        a.append(arr[i])
        i+=1
    while(j<high+1):
        a.append(arr[j])
        j+=1
    for i in range(low,high+1):
        arr[i]=a[i-low]

def sort(arr,low,high):
    if(low<high):
        mid=(low+high)//2
        sort(arr,low,mid)
        sort(arr,mid+1,high)
        marged(arr,low,mid,high)

def dist2(arr):
    sort(arr,0,len(arr)-1)
    min_dist=9999999
    for i in range(len(arr)-1):
        if(abs(arr[i]-arr[i+1])<min_dist):
                min_dist=abs(arr[i]-arr[i+1])
    return min_dist


arr= [30,5,20,9]
print(dist(arr))
print(dist2(arr))

