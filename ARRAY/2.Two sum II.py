# Example 1:

# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
# Example 2:

# Input: numbers = [2,3,4], target = 6
# Output: [1,3]
# Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
# Example 3:

# Input: numbers = [-1,0], target = -1
# Output: [1,2]
# Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].

def s(numbers,target):
    i=0
    j=len(numbers)-1
    while(i<j):
        if(numbers[i]+numbers[j]==target):
            li=[]
            li.append(i+1)
            li.append(j+1)
            return li
        elif(numbers[i]+numbers[j]<target):
            i+=1
        else:
            j-=1
        
print(s([-1,0],-1))
