# 240. Search a 2D Matrix II

# Write an efficient algorithm that searches for a 
# value target in an m x n integer matrix matrix. This 
# matrix has the following properties:

# Integers in each row are sorted in ascending from left to right.
# Integers in each column are sorted in ascending from top to bottom.

# Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
# Output: true

# Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
# Output: false


def Binary_Search(arr,target):
    row = len(arr)
    column = len(arr[0])
    row_index = 0
    col_index = column-1

    while(row_index<row and col_index>=0):
        element = arr[row_index][col_index]

        if(element==target):
            return "Found"
        elif(element<target):
            row_index+=1
        else:
            col_index-=1
    return "Not Found"

arr = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]

print(Binary_Search(arr,24))
