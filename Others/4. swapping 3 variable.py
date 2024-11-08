#  a=10, b=20, c=30
#  => a=30, b=10, c=20

#  Using Arithmetic process:-
def arith(a,b,c):
    a= a+b+c 
    b= a-(b+c) # a+b+c- b-c = a
    c= a-(b+c) # a+b+c -a-c = b
    a= a-(b+c) # a+b+c -a-b = c

    return a,b,c

a=10
b=20
c=30
print(a,b,c)

a,b,c = arith(a,b,c)
print(a,b,c)


