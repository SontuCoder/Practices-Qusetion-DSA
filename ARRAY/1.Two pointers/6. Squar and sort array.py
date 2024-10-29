#Leetcode:- 977
# IO:- [-4,-1,0,3,10,13] ==> [0,1,9,16,100,169]
# Note: Array is Sorted.

# Method 1: Sort acording Absolute value -> Squar liniarly ...O(n*logn) 
# Method 2: Squar Liniarly -> sort ..O(n*logn) 
# Method 3: By two pointers: takes O(n) 
#       
#           a. Find Minimum number index of abs acording abs value.
#           b. i=j=indexof(min_num) ..(like 2 = indexof(0))
#           c. insert in it in new arr
#           d. i--, j++
#           e. do step f-g until( i>=0 and j<len(arr))
#           f. if(sqr(arr[i])>sqr(arr[j])):
#                  insert sqr(arr[j]) in to new arr and j++
#           g. else
#                  insert sqr(arr[i]) in to new arr and i--
#           h. insert others all elements squrs 

# Method 4: By Two pointer takes O(n)
#            
#         a. i=0, j=len(arr)-1
#         b. do step c-d until( i<j)
#         c. if(sqr(arr[i])>sqr(arr[j])):
#                  insert sqr(arr[j]) in to new arr and j--
#         d. else
#                  insert sqr(arr[i]) in to new arr and i++


#Method 3
def squr_sort(arr):
    a=0
    for i in range(len(arr)):
        if(abs(arr[a])>abs(arr[i])):
            a=i
    nums=[]
    nums.append(arr[a]**2)
    i=a-1
    j=a+1
    while(i>=0 and j<len(arr)):
        if((arr[i]**2)>(arr[j]**2)):
            nums.append((arr[j]**2))
            j+=1
        else:
            nums.append((arr[i]**2))
            i-=1
    while(i>=0):
        nums.append((arr[i]**2))
        i-=1
    while(j<len(arr)):
        nums.append((arr[j]**2))
        j+=1
    return nums


#Method 4:
def squr_sort2(arr):
    i=0
    j=len(arr)-1
    nums=[]
    while(i<=j):
        if(i==j):
            nums.insert(0,arr[i]**2)
            i+=1
            j-=1
        elif((arr[i]**2)<(arr[j]**2)):
            nums.insert(0,arr[j]**2)
            j-=1
        else:
            nums.insert(0,arr[i]**2)
            i+=1
    return nums


arr=[-4,-1,0,3,10,13]
print(squr_sort2(arr))