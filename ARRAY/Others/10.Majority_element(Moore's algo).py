# Majority element: which eleement appears more then n/2 time.

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

arr=[3,3,3,4,4,4,3,5,3]
print(moores(arr))