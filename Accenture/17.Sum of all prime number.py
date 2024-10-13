# find sum of all prime numbers till N.
#IO: 8
#OP: 17..(2,3,5,7)

def prime(n):
    s=0
    for i in range(2,n):
        if(n%i==0):
            s+=1
            break
    if(s==0):
        return True
    return False

def sum_prime(N):
    sum=0
    if(N<2):
        return 0
    if(N==2):
        sum+=N
    for i in range(2,N+1):
        if(prime(i)):
            sum+=i
    return sum

N=8
print(sum_prime(N))
