# Find first K words of a string.

#IO: "my name is Subhadip Maity", 3 ==> "my name is"
#IO: "hello world kabla", 1 ==> "hello"

def k_word(S,N):
    k=""
    count=0
    for i in range(len(S)):
        if(S[i]==" " and count < N):
            count += 1
        if(count==N):
            return k
        k+= S[i]

S="my name is Subhadip Maity"
N=2
print(k_word(S,N))