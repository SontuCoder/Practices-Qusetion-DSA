# Count minimum right flips to set all values in an array

# N light bulbs are connected by a wire. Each bulb has a switch associated with it,
# however due to faulty wiring, a switch also changes the state of all the bulbs to
# the right of current bulb. Given an initial state of all bulbs, Find the minimum
# number of switches you have to press to turn on all the bulbs. You can press the 
# same switch multiple times.

# Note: O represents the bulb is off and 1 represents the bulb is on.

# A[] = [0,1,0,1] 
# o/p = 4

def flip(A):
    count=0
    for i in range(len(A)):
        if(count%2==0):
            if(A[i]==0):
                count+=1
            else:
                continue
        elif(count%2==1):
            if(A[i]==0):
                continue
            else:
                count+=1
    return count

A=[0,1,1,0,1,0]
print(flip(A))