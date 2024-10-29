# find element from 2d array:- 

def  find_in_2D(arr,num):
    colum = len(arr[0]) 
    row = len(arr)
    for i in range(row):
        for j in range(colum):
            if(arr[i][j]==num):
                return 1
    return 0

arr=[[1,2,3],[4,5,6],[7,8,9]]
if(find_in_2D(arr,6)):
    print("Found")
else:
    print("not found")
