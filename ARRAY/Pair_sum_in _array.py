# in:- [1,4,2,4,6,5],3
#Op:- [1,2]
# TWO methods take O(n) time.

# def pair(arr,x):
#     s=set()
#     for i in arr:
#         temp= x-i
#         if(temp in s):
#             return temp,i
#         else:
#             s.add(i)
#     return False

def pair(arr,x):
    s=[0]*100
    for i in range(len(arr)):
        temp= x-arr[i]
        if(s[temp]==1):
            for j in range(len(arr)):
                if(arr[j]==temp):
                    return j,i
        else:
            s[arr[i]]=1
    return False

arr=[1,4,2,4,6,5] 
x=10
print(pair(arr,x))