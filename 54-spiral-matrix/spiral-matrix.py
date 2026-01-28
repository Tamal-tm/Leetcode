class Solution(object):
    def spiralOrder(self, matrix):
        if not matrix or not matrix[0]:
            return []

        result=[]
        # Initialize pointers for traversal.
        top,left=0,0
        bottom,right=len(matrix)-1,len(matrix[0])-1

        # Traverse the matrix in spiral order
        while top <=bottom and left <=right:
            # Move left to right across the top row.
            for i in range(left,right+1):
                result.append(matrix[top][i])
            top+=1

            # Move top to botton along the right column.
            for i in range(top, bottom+1):
                result.append(matrix[i][right])
            right -=1
        
            # Move right to left across the bottom row (if still valid)
            if top <=bottom:
                for i in range(right, left-1, -1):
                    result.append(matrix[bottom][i])
                bottom -=1
            
            # Move bottom to top alobe the left columns ( if valid)
            if left <= right:
                for i in range(bottom, top-1, -1):
                    result.append(matrix[i][left])
                left +=1
        
        return result

        