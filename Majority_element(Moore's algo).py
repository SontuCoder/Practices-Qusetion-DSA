def moores(arr):
    maj_index=0
    count=1
    for i in range(1,len(arr)):
        if(arr[maj_index]==arr[i]):
            count+=1
        else:
            count-=1
        if(count==0):
            maj_index=i
            count=1
    return arr[maj_index]

arr=[3,3,3,1,3,5,4,3,2]

print(moores(arr))