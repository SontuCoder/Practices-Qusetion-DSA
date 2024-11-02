def zigzag(s, n):
    if n==1 : return s
    res = ""
    for r in range(n):
        incre = 2* (n-1)
        for i in range(r, len(s), incre):
            # print(r,i)
            res += s[i]
            if(r>0 and r<n and i+incre - 2*r <len(s)):
                # print(r,i+incre - 2*r)
                res += s[i+incre - 2*r]
        
    return(res)


# Test the function
s = "PAYPALISHIRING"
print(zigzag(s, 4))

