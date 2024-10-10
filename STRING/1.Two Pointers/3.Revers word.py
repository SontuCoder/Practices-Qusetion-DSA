# Write a function that reverses a string. The input string is given as an array of characters s.

#IO: "Sontu" ==> "utnoS"
#IO: "jsww" ==> "wwsj"

# Method 1: (worng method)
def revers(s):
    for i in range(len(s)//2):
        s[i], s[len(s)-1-i] = s[len(s)-1-i], s[i]
    return s

# Method 2:
def rev(s):
    li=[]
    for i in range(len(s)): # also use list() method
        li.append(s[i])
    new_str = ""
    for i in range(len(li)-1,-1,-1):
        new_str+=li[i]
    return new_str


s="Sontu"
print(rev(s))


# same parten for reverse of number. (1234=>4321)