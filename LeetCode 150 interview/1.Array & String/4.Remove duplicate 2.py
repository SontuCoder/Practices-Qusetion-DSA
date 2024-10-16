# LeetCode 80

def duplicate(arr):
    prev=0
    i=1
    count=1
    while(i<len(arr)):
        if(arr[i]!=arr[prev]):
            prev=i
            count=1
            i+=1
        else:
            if(count==2):
                arr.pop(i)
            else:
                count+=1
                i+=1
    return  len(arr)

arr=[1,1,1,2,2,3,3,3,4]
print(duplicate(arr))




