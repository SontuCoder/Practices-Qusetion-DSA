# IO: [1,4,5,7,9], [4,5,7,9] => [1]
# IO: [2,3,4,5], [2,3,4,5,6] => [6]


def find(arr1,arr2,m):
    if(m==1):
        return arr1[0]
    if(arr1[0] !=arr2[0]):
        return arr1[0]
    i=0
    h=m-1
    while(i<h):
        mid=(i+h)//2
        if(arr1[mid]==arr2[mid]):
            i=mid
        else:
            h=mid
        if(i==h-1):
            break
    return arr1[h]


def lost(arr1,arr2):
    if(len(arr1)==len(arr2)):
        return "Invalid"
    if(len(arr1)>len(arr2)):
        return find(arr1,arr2,len(arr1))
    else:
        return find(arr2,arr1,len(arr2))
    

arr1=[4,5,7,9]
arr2=[4,5,7,9]
print(lost(arr1,arr2))
