# use for Maximum subarray Sum in O(n):

def kadane(arr):
    if(len(arr)==0):
        return -1
    if(len(arr)==1):
        return arr[0]
    current_max=global_max=arr[0]
    for i in range(1,len(arr)):
        current_max = max(current_max+arr[i],arr[i])
        global_max = max(current_max,global_max)
    return global_max

def kadane_recur(arr,i,curr_max,global_max):  #Ensure that len(arr)>0
    if(i==len(arr)):
        return global_max
    curr_max= max(curr_max+arr[i],arr[i])
    global_max = max(curr_max,global_max)
    return kadane_recur(arr,i+1,curr_max,global_max)




arr=[1,3,1,-4,5,-8,2]
print(kadane(arr))
print(kadane_recur(arr,1,arr[0],arr[0]))



