# Array have +ve -ve.You need to find two element
# such sum is closest to zero.

#IO: [1,60,-10,70,-80, 85]
# OP: [-80,85]


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

def sum(arr):
    sort(arr,0,len(arr)-1)
    i=0
    j=len(arr)-1
    s=9999999
    a=[]
    while(i<j):
        if(s>abs(arr[i]+arr[j])):
            s=(arr[i]+arr[j])
            a.clear()
            a.append(arr[i])
            a.append(arr[j])
        if((arr[i]+arr[j])>0):
            j-=1
        elif((arr[i]+arr[j])<0):
            i+=1
        else:
            a.clear()
            a.append(arr[i])
            a.append(arr[j])
            break
    return a

arr=[1,2,-10,70,-80, 85]
print(sum(arr))
