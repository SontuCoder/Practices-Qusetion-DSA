#  Your task is to write a function that returns the
#  maximum number if pieeces that can be obtained by 
#  making N number of cuts.

# Note: if a chord of circle cuts n often chords then 
#       it wike intrduce (n+1) new cuts.

# N = total number of pices, n = cuts
def cuts(n):
    if(n==0):
        return 1
    else:
        N=1
        for i in range(n):
            N+=(i+1)
        return N

n=8
print(cuts(n))