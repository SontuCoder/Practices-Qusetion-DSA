# IO: "[](){}" ==> True
#IO: "{)" ==> false
#IO: "((((()))))" ==> true
#IO: "[()]()" ==> true


# Method 1. Using stack O(n) time
def paren(s):
    if len(s) == 0:
        return True 
    li = []
    for i in range(len(s)):
        if s[i] in "({[":
            li.append(s[i])
        elif len(li) > 0 and ((li[-1] == "(" and s[i] == ")") or (li[-1] == "{" and s[i] == "}") or (li[-1] == "[" and s[i] == "]")):
            li.pop() 
        else:
            return False 
        print(li)
    return len(li) == 0

s="{)"
print(paren(s))