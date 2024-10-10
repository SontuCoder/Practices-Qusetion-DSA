#Check If One String Is Rotation Of Another String

#IO: "abcd", "cdab" ==> true
#IO: "abcd", "bacd" ==> false

# Method 1:
def check(s1,s2):
    if(len(s1)!=len(s2)):
        return "false"
    s=s1+s1
    str_ind=0
    m=0
    for i in range(len(s)-len(s2)):
        if(s[i]==s2[0]):
            str_ind=i
            m+=1
            break
    if(m==1):
        for j in range(len(s2)):
            if(s2[j]!=s[j+str_ind]):
                return "false"
        return "true"
    return "false"


# Method 2:
def check_2(s1,s2):
    if(len(s1)!=len(s2)):
        return "false"
    str_ind=0
    m=0
    for i in range(len(s1)):
        if(s1[i]==s2[0]):
            str_ind=i
            m+=1
            break
    if(m==1):
        for j in range(len(s2)):
            if(s2[j]!=s1[(j+str_ind)%len(s1)]):
                return "false"
        return "true"
    return "false"



s1="abcd"
s2="cdab"
print(check(s1,s2))
print(check_2(s1,s2))