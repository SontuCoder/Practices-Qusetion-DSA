
# Find common elements in three sorted arrays

# array1[] = {1, 5, 5)
# array2[] = {3, 4, 5, 5, 10}
# array3[] = {5, 5, 10, 20}
# Output: 5, 5

# using 3 ptr , takes O(len(a1), len(a2), len(a3)):
def common(arr1,arr2,arr3):
    i=j=k=0
    li=[]
    while(i<len(arr1) and j<len(arr2) and k<len(arr3)):
        if(arr1[i]==arr2[j] and arr1[i]==arr3[k]):
            li.append(arr1[i])
            i+=1
            j+=1
            k+=1
        elif(arr1[i]<arr2[j]):
            i+=1
        elif(arr2[j]<arr3[k]):
            j+=1
        else:
            k+=1

    if(len(li)):
        return li
    return "none"

array1 = [1, 5, 5]
array2 = [3, 4, 10]
array3 = [5, 5, 10, 20]

print(common(array1,array2,array3))