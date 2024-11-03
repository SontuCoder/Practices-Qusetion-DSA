#  Is Subsequence:- 392

def is_subsequence(s,t):
    i=0
    j=0
    count=0
    while(i<len(s) and j<len(t)):
        if(s[i]==t[j]):
            i+=1
            j+=1
            count+=1
        else:
            j+=1
    if(count==len(s)):
        return True
    return False

s="acb"
t="ahbgdc"
print(is_subsequence(s,t))