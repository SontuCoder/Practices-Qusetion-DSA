# 3Sum :- 15

def three_sum(nums):
    nums.sort()
    li=set()
    for i in range(0,len(nums)-2):
        if i > 0 and nums[i-1]==nums[i]:
            continue
        j=i+1
        k=len(nums)-1
        while(j<k):
            total = nums[i]+nums[j]+nums[k]
            if(total==0):
                li.add((nums[i],nums[j],nums[k]))
                j+=1
                k-=1
            elif(total<0):
                j+=1
            else:
                k-=1
    return list(li)

arr=[-1,0,1,2,-1,-4]
print(three_sum(arr))
