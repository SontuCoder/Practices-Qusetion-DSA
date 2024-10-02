from collections import Counter

def unique(a):
    b=list(Counter(a).values())
    i=0
    li=[]
    while(i<len(b)):
        if(b[i] in li):
            return 0
        else:
            li.append(b[i])
        i+=1
    return li

a=[1,2,2,3,3,3]
print(unique(a))