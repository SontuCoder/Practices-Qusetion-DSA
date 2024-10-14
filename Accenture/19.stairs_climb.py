# → Alice has a pair of magical shoes that allows her to climb 3 
# stairs at once. In the city there are N houses whose roof Alice
# wants to reach. The number of roofs of each house is given in an array A.
# Alice can reach the roof of only those houses where the number is 
# a multiple of 3. Your task is to find and return integer value 
# representing the count of the number of houses whose roof Alice can climb.

# IP:[12,16,21.20] ==> 2 ..(12,21)

# IP: [6] ==> 1

def stairs(arr):
    count=0
    for i in range(len(arr)):
        if(arr[i]%3==0):
            count+=1
    return count

arr=[12,16,21,20]
print(stairs(arr))