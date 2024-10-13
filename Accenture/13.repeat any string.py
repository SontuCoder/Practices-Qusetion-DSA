# You are Given an Integer N and a string S. Your task is find 
# and return new string which consist of the original string 
# repeated N times.

# IO: "ABC", 3 ==> "ABCABCABC"


def repeated(S,N):
    ans=""
    while(N!=0):
        ans+= S
        N-=1
    return ans

S= "ABC"
N=3
print(repeated(S,N))