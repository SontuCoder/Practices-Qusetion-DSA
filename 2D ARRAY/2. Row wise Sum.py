# Row wise Sum Of a array:- 
# Next task: Largest Row return:

def row_sum(arr):
    li=[]
    colum = len(arr[0]) 
    row = len(arr)
    for i in range(row):
        s=0
        for j in range(colum):
            s+=arr[i][j]
        li.append(s)
    return li

def col_sum(arr):
    li=[]
    colum = len(arr[0]) 
    row = len(arr)
    for i in range(colum):
        s=0
        for j in range(row):
            s+=arr[j][i]
        li.append(s)
    return li


arr=[[1,2,3],[4,5,6],[7,8,9]]
print(row_sum(arr))
print(col_sum(arr))

