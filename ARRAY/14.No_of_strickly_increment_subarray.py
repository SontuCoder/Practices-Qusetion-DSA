#In:- [1,4,3]
#Op:- 1 ..([1,4])

#In:- [1,2,3,4]
#OP:- 6,... ([1,2],[2,3],[3,4],[1,2,3],[2,3,4],[1,2,3,4])

#Law of subArray in an array :- (n*(n+1))/2
# It takes O(n) time

def subArray(arr):
    length=0
    cout=0
    for i in range(0,len(arr)-1):
        if(arr[i+1]>arr[i]):
            length+=1
        else:
            cout+=((length*(length+1))//2)
            length=0
    if(length>0):
        cout+=((length*(length+1))//2)
    return cout

arr = [1,2,3,4]
print(subArray(arr))