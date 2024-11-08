# Print pattern 1 1 2 4 3 9 4 16.

def squar_pattern(n):
    for i in range(1,n+1):
        print(i, end=" ") # for "end = " " "it print in same line
        print(i*i, end=" ")

n=4
squar_pattern(n)