# LeetCode: 345
# IO: "hello" => "holle"
#IO: "leetcode" => "leotcede"
# Complete it in O(n) time


def rev_vow(string):
    s=list(string)
    low_vow="aeiouAEIOU"
    i=0
    j=len(s)-1
    while(i<j):
        if(s[i] not in low_vow):
            i+=1
        if(s[j] not in low_vow):
            j-=1
        if(s[i] in low_vow and s[j] in low_vow):
            s[i], s[j] =  s[j], s[i]
            i+=1
            j-=1
    return ''.join(s)

s = "leetcode"
print(rev_vow(s))
