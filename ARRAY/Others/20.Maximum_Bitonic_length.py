# IO: [12,4,78,90,45,23], inc[]=> [1,1,2,3,1,1]
# dec[]=> [2,1,1,3,2,1]
#return max(inc[i]+dec[i]-1)

def inc_Bit(arr):
    j=1
    a=[]
    a.append(1)
    for i in range(1,len(arr)):
        if(arr[i]>arr[i-1]):
            j+=1
            a.append(j)
        else:
            j=1
            a.append(j)
    return a

def dec_Bit(arr):
    j=1
    a=[]
    a.append(1)
    for i in range(len(arr)-1,0,-1):
        if(arr[i]<arr[i-1]):
            j+=1
            a.insert(0,j)
        else:
            j=1
            a.insert(0,j)
    return a


def bitonic(arr):
    inc=inc_Bit(arr)
    dec=dec_Bit(arr)
    m=0
    for i in range(len(inc)):
        if(m<(inc[i]+dec[i]-1)):
            m=inc[i]+dec[i]-1
    return m

arr=[12,4,78,90,45,23]
print(bitonic(arr))