# LeetCode: 15,16,259

# nums = [-1,0,1,2,-1,-4], 0
# Output: [[-1,-1,2],[-1,0,1]]

# nums = [0,1,1]
# Output: [] ..It not posible.

# nums = [0,0,0], 0
# Output: [[0,0,0]] ...0+0+0=0

def Sum3(arr,target):
    li=[]
    arr.sort()
    for i in range(len(arr)-2):
        j=i+1
        k=len(arr)-1
        while(j<k):
            if(arr[i]+arr[j]+arr[k]==target):
                a=[]
                a.append(arr[i])
                a.append(arr[j])
                a.append(arr[k])
                if(a not in li):
                    li.append(a)
                j+=1
                k-=1
            elif(arr[i]+arr[j]+arr[k]<target):
                j+=1
            else:
                k-=1
    if(len(li)):
        return li
    return "Not posible"

arr= [0,1,1]

print(Sum3(arr,0))
