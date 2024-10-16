#LeetCode 88

def marge_sort(arr1,m,arr2,n):
    i=0
    j=0
    a=[]
    while(i<m and j<n):
        if(arr1[i]<arr2[j]):
            a.append(arr1[i])
            i+=1
        else:
            a.append(arr2[j])
            j+=1
    while(i<m):
        a.append(arr1[i])
        i+=1
    while(j<n):
        a.append(arr2[j])
        j+=1
    return a

arr1=[1,2,3,0,0,0]
m=3
arr2=[2,5,6]
n=3
print(marge_sort(arr1,m,arr2,n))