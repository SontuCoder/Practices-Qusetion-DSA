# For a given two-dimensional integer array/list 'ARR' 
# of size (N x M), print the 'ARR' in a sine wave 
# order, i.e., print the first column top to bottom,
# next column bottom to top, and so on.

# For eg:-
# The sine wave for the matrix:-
# IP:- [[1,2],[3,4]]
# OP:- (1, 3, 4, 2)

def wave_print(arr):
    li=[]
    row = len(arr)
    column = len(arr[0])
    for i in range(column):
        if(i%2==0):
            for j in range(row):
                li.append(arr[j][i])
        else:
            for j in range(row-1,-1,-1):
                li.append(arr[j][i])
    return li


arr = [[1,2,3],[4,5,6],[7,8,9]]
print(wave_print(arr))

