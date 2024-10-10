# Given an integer x, return true if x is a 
#palindrome, and false otherwise.

#IO: "abba" ==> true
#IO: "anjsa" ==> false


# Method single pointer:
def palindrom(s):
    for i in range(len(s)//2):
        if(s[i] != s[len(s)-i-1]):
            return 'false'
    return 'true'

#Method two pointers:
def palin(s):
    i=0
    j=len(s)-1
    while(i<j):
        if(s[i]!=s[j]):
            return 'false'
        i+=1
        j-=1
    return 'true'

s="dabbad"
print(palindrom(s))
print(palin(s))
