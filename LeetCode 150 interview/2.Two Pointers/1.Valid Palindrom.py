# Valid Palindrom - 125

def is_valid(s):
    s=s.lower()
    i=0
    j=len(s)-1
    while(i<j):
        if((s[i]>= "a" and s[i]<= "z") or(s[i]>= "0" and s[i]<= "9")):
            if((s[j]>= "a" and s[j]<= "z")or(s[j]>= "0" and s[j]<= "9")):
                if(s[i]!=s[j]):
                    return False
                else:
                    j-=1
                    i+=1
            else:
                j-=1
        else:
            i+=1
    return True


s = "0P"
print(is_valid(s))