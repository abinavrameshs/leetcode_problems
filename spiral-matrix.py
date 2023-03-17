"""
Problem : Spiral Matrix
https://leetcode.com/problems/spiral-matrix/description/

"""

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        lst = []
        n_rows, n_cols = len(matrix), len(matrix[0])
        direction = 'right'
        flag = True
        while flag : 
            if direction == 'right' : 
                # if direction == 'right', then loop through n_cols with row as 0
                for j in range(n_cols) : 
                    lst.append(matrix[0][j]) 
                direction = 'down'
                # Cut off the first row of the matrix
                matrix = matrix[1:]
            elif direction == 'down' : 
                # if direction == 'down', then loop through n_rows from top to bottom and the column fixed as last column
                for j in range(n_rows):
                    lst.append(matrix[j][n_cols-1]) 
                direction = 'left'
                # Cut off the last column of the matrix
                matrix = list(map(lambda x : x[:(n_cols-1)],matrix))
            elif direction == 'left' : 
                # if direction == 'left', then loop through n_cols in reverse from right to left keeping the row fixed as the last row
                for j in range(n_cols-1,-1,-1):
                    lst.append(matrix[n_rows-1][j]) 
                direction = 'up'
                # Cut off the last row of the matrix
                matrix = matrix[:-1]
            elif direction == 'up' : 
                # if direction == 'up', then loop through n_rows in reverse from bottom to top keeping the column fixed as the first column
                for j in range(n_rows-1,-1,-1):
                    lst.append(matrix[j][0]) 
                direction = 'right'
                # Cut off the first column of the matrix
                matrix = list(map(lambda x : x[1:],matrix))
                
            # Update n_rows, n_cols if the matrix!=[] or the number of columns!=0
            if matrix !=[] and len(matrix[0]):
                n_rows, n_cols = len(matrix), len(matrix[0])  
            else : 
                flag = False
        return lst
