# You are working on a financial analysing tool which represents
# daily stock prices of a company over time. Each element in an 
# integer array A of size N represents the closing price of the 
# stock for that particular day. Your task is to find and return 
# an integer value representing the total number of days where 
# the stock market price decreased indicating negative growth.

# I/p: [1,2,3,1,4,5,2] ==> 2..(1,2)
# I/P: [6] ==> 0

def stock(arr):
    if(len(arr)<2):
        return 0
    count=0
    for i in range(1,len(arr)):
        if(arr[i]<arr[i-1]):
            count+=1
    return count

arr= [1,2,3,1,4,5,2] 
print(stock(arr))