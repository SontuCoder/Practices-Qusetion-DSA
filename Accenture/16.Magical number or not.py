# Find count of Magical numbers from 1 to N.
# A Number is magical if:
#     -> Convert to binary.
#     -> Replace 0 with 1 and 1 with 2 in binary string.
#     -> Calculate Sum af all digits in binary string.
#     -> Resultant must be ODD number.

#IO: 5 ==> 2 ..{   1-> 1 -> 2
                #  2-> 10-> 21-> 3
                #  3-> 11-> 22-> 4
                #  4-> 100-> 211-> 4
                #  5-> 101-> 212-> 5}

def sum_replace_binary(n):
    k=0
    while(n!=0):
        if(n%2==0):
            k+=1
        n//=2
    return k

def magical_number(N):
    count=0
    for i in range(1,N+1):
        if(sum_replace_binary(i)%2==1):
            count+=1
    return count

N=6
print(magical_number(N))