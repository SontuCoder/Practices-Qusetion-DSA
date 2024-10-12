#Problem Description:
# The Binary number system only uses two digits, 0 and 1 and number system can be called binary string.
# You are required to implement the following function: int OperationsBinaryString(dringer);
# The function accepts a string str as its argument. The string str consists of binary digits eparated with an alphabet as follows:
# A denotes AND operation
# B denotes OR operation
# C denotes XOR Operation
# You are required to calculate the result of the string str, scanning the string to right taking one opearation at a time, and return the same.

# Note:
# No order of priorities of operations is required
# Length of str is odd
# If str is NULL or None (in case of Python), return -1

#IO: "1C0C1C1A0B1" ==> 1
#IO: "1A0B1" ==> 1

def operation(s):
    if(len(s)==0):
        return -1
    ans=int(s[0])
    for i in range(2,len(s),2):
        if(s[i-1]=="A"):
            ans= ans and int(s[i])
        elif(s[i-1]=="B"):
            ans= ans or int(s[i])
        elif(s[i-1]=="C"):
            ans= ans ^ int(s[i])
    return ans

s="1A0B1"
print(operation(s))