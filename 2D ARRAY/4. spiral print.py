# Spiral Print a N*M array.

# IP:- [[1,2,3],[4,5,6],[7,8,9]] ==> [1,2,3,6,9,8,7,4,5]

def spiral_print(arr):
    str_row = 0
    end_row = len(arr)
    str_column = 0
    end_column = len(arr[0])
    direction = "lr"
    li=[]
    element = end_column*end_row
    while(len(li)<element):
        if(direction == "lr"):
            for i in range(str_column, end_column):
                li.append(arr[str_row][i])
            str_row+=1
            direction = "ud"
        elif(direction == "ud"):
            for i in range(str_row, end_row):
                li.append(arr[i][end_column-1])
            end_column-=1
            direction = "rl"
        elif(direction == "rl"):
            for i in range(end_column-1,str_column-1,-1):
                li.append(arr[end_row-1][i])
            end_row-=1
            direction = "du"
        elif(direction=="du"):
            for i in range(end_row-1,str_row-1,-1):
                li.append(arr[i][str_column])
            str_column+=1
            direction = "lr"
    return li

arr = [[1,2,3],[4,5,6],[7,8,9],[0,0,0]]
print(spiral_print(arr))

