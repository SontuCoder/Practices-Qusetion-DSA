# Given an m x n matrix, return all elements of the matrix in spiral order.
# Example 1:
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]

# Example 2:
# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]

def spiralOrder(matrix):
        der=1
        top=0
        left=0
        down=len(matrix)-1
        right=len(matrix[0])-1
        li=[]
        while(top<=down and right>=left):
            if(der==1):
                i=left
                while(i<=right):
                    li.append(matrix[top][i])
                    i+=1
                top+=1
                der=2
            elif(der==2):
                i=top
                while(i<=down):
                    li.append(matrix[i][right])
                    i+=1
                right-=1
                der=3
            elif(der==3):
                i=right
                while(i>=left):
                    li.append(matrix[down][i])
                    i-=1
                down-=1
                der=4
            elif(der==4):
                i=down
                while(i>=top):
                    li.append(matrix[i][left])
                    i-=1
                left+=1
                der=1
        return li


matrix= [[1,2,3,4],[5,6,7,8],[9,10,11,12],[81,23,1221,323]]
print(spiralOrder(matrix))
