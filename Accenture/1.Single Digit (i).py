#  Given a number N your taksk is to make N  in a Single digit.
#  By following operations:

#  (i) if N is Odd make it floor (N/2).
#  (ii) if N is even make it floor ((N-2)/2).
#  (iii) if N is already a single digit print it as it is.

#  IO: 10 ==> 4
#  IO: 12 ==> 5
#  IO: 55 ==> 6
#  IO: 8  ==> 8

def single(N):
    while(N>9):
        if(N%2==0):
            N=((N-2)//2)
        else:
            N=N//2
    return N
    
N=55
print(single(N))