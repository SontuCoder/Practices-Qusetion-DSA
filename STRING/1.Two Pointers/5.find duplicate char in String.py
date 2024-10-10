# Find the Duplicate character in a String.

#IO: "ksnxqkxxkas" ==> [["k",3],["s",2]] or, [["s",2], ["k",3]]

# Method 1:
from collections import Counter
def dupli(s):
    li= Counter(s)
    list_dupli = []
    list_keys = li.keys()
    for i in list_keys:
        if(li[i]!=1):
            a=[]
            a.append(i)
            a.append(li[i])
            list_dupli.append(a)
    return list_dupli

# Method 2:
def duplicate(s):
    li=[0]*(ord("z")-ord("a")+1)
    for i in s:
        li[ord(i)-ord("a")]+=1
    list_dupli = []
    for i in range(len(li)):
        if(li[i]>1):
            a=[]
            a.append(chr(i+ord("a")))
            a.append(li[i])
            list_dupli.append(a)
    return list_dupli


s= "ksnxqkxxkas"
print(dupli(s))
print(duplicate(s))


