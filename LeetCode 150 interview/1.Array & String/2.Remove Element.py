# Leetcode 27

def remove(arr,k):
    count = 0
    for i in arr:
        if(i==k):
            count+=1
    return len(arr)-count

arr=[3,2,2,3]
print(remove(arr,3))
