# Reverse an array without affecting special characters
# Given a string, that contains special character
# together with alphabets ('a' to 'z' and 'A' to 'Z'), 
# reverse the string in a way that special characters 
# are not affected.

# Input: str = "a,b$c"
# Output: str = "c,b$a"

# Note that $ and, are not moved anywhere.
# Only subsequence "abc" is reversed

# Input: str = "Ab, c, de!$"
# Output: str = "ed,c,bA!$"

def rever(s):
    s = list(s)
    i=0
    j=len(s)-1
    a= "abcdefghijklmnopqrstuvwxyz"
    A= "QWERTYUIOPLKJHGFDSAZXCVBNM"
    while(i<j):
        if(s[i] not in a and s[i] not in A):
            i+=1
        elif(s[j] not in a and s[j] not in A):
            j-=1
        else:
            s[i], s[j] = s[j], s[i]
            i+=1
            j-=1
    return "".join(s)

s= "c,b$a"
print(rever(s))



