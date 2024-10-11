# Rearrangement Of Bits:

# Alex Gives You a positive Number N and wants you
# to rearrange the bits of the number in its binary
# representation such that all set bits are in consecutive order.
# Your task is to find and return an integer value
# representing the minimum possible number that can be 
# formed after re-arranging the bits of the number N.

#IO: 10 ==> 3 ..( 10 -> 1010 -> in consecutive order means all 1 's together, 
#                in such we get 3 items [1100,0110,0011], smallest is 0011 -> 3)

#IO: 2 ==> 1
#IO: 11 ==> 7 ..(1011 -> [1110, 0111] -> 0111 -> 7)

# steps: 1. Retrive binary numbers and and count 1's.
#        2. Arrenge all 1's in last side.
#        3. convert it in Decimale.

def rearrange_bits(N):
    count=0
    while(N!=0):
        if(N%2):
            count+=1
        N=N//2

    return (2**count)-1
N=4
print(rearrange_bits(N))