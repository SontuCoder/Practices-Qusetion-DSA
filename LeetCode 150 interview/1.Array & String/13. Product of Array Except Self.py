#LeetCode: 238

# Method 1 : using Prefix product and Sufix product
#  takes O(n)

def product_except_self(arr):
    prefix=[0]*len(arr)
    sufix=[0]*len(arr)
    pro=1
    for i in range(len(arr)):
        prefix[i]=pro
        pro=pro*arr[i]
    pro=1
    for i in range(len(arr)-1,-1,-1):
        sufix[i]=pro
        pro=pro*arr[i]
    for i in range(len(prefix)):
        arr[i]=prefix[i]*sufix[i]
    return arr

arr=[1,2,3,4]
print(product_except_self(arr))