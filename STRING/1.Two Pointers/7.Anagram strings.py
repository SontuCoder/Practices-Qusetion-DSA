# Check if two strings are anagrams

#IO: s1="silent", s2="lisent" ==> yes
#IO: s1="abcd", s2="acbd" ==> yes
#IO: s1="bsh", s2="bhd" ==> no
#IO: s1="ajnn", s2="ajn" ==> no

# Method 1: takes O(nlogn) time in sorting
def anagram(s1,s2):
    if(len(s1)!=len(s2)):
        return "no"
    s1=sorted(s1) 
    s2=sorted(s2)
    for i in range(len(s1)):
        if(s1[i]!=s2[i]):
            return "no"
    return "yes"

# Method 2: takes O(n)
def ana(s1,s2):
    if(len(s1)!=len(s2)):
        return "no"
    li=[0]*(ord("z")-ord("a")+1)
    for i in s1:
        li[ord(i)-ord("a")]+=1
    for i in s2:
        if(li[ord(i)-ord("a")]>0):
            li[ord(i)-ord("a")]-=1
        else:
            return "no"
    for i in range(len(li)):
        if(li[i]!=0):
            return "no"
    return "yes"

s1="silent"
s2="lisent"
print(anagram(s1,s2))
print(ana(s1,s2))