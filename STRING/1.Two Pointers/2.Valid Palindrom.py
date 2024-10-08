# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

# Example 2:

# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.

# Example 3:

# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.

def pal(s):
    a=s.lower()
    b=list(a)
    li=[]
    for i in b:
        if(ord(i)>96 and ord(i)<123):
            li.append(i)
    print(li)
    j=0
    k=len(li)-1
    while(j<k):
        if(li[j]!=li[k]):
            return "false"
        j+=1
        k-=1
    return "true"


s = "race a car"
print(pal(s))