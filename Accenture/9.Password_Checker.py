# check the given password is valid or not.

# Rules:
#       1. At least 4 chars.
#       2. At least 1 numeric.
#       3. At least one capitail leater.
#       4. No space or slash(/).
#       5. starting char must not be numeric.

def check(s):
    count=[0]*5
    if(len(s)>=4):
        count[0]=1
    if(s[0]>="0" and s[0]<="9"):
        count[4]=1
    for i in range(1,len(s)):
        if(ord(s[i])>=65 and ord(s[i])<=90):
            count[2]=1
        if(s[i] >="0" and s[i]<="9"):
            count[1]=1
        if(s[i]==" " or s[i]=="/"):
            count[3]=1
    for i in range(3):
        if(count[i]==0):
            return False
    for i in range(3,5):
        if(count[i]==1):
            return False
    return True

s="ejn3"

print(check(s))

