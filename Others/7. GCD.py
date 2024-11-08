# GCD of two numbers:-

def gcd(m,n):
    if(n==0):
        return m
    else:
        return gcd(n, m%n)

m = 39
n = 25
print(gcd(m,n))