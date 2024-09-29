#Io: [88,105,3,2,200,0,10]
# Op: 1, 4-9,11-87, 89-99

#Time O(n)

def missing(arr):
    s=[0]*101
    for i in arr:
        if(i>=0 and i<100):
            s[i]=1
    s[100]=1
    a=[]
    count=0
    for i in range(101):
        if(s[i]!=0):
            if(count>1):
                a.append(f"{i-count}-{i-1}")
                count=0
            if(count==1):
                a.append(f"{i-1}")
                count=0
        else:
            count+=1
    return a
arr=[9,6,900,850.5,90,100,99]
print(missing(arr))
