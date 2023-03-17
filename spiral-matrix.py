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
                for j in range(n_cols) : 
                    lst.append(matrix[0][j]) 
                direction = 'down'
                matrix = matrix[1:]
            elif direction == 'down' : 
                for j in range(n_rows):
                    lst.append(matrix[j][n_cols-1]) 
                direction = 'left'
                matrix = list(map(lambda x : x[:(n_cols-1)],matrix))
            elif direction == 'left' : 
                for j in range(n_cols-1,-1,-1):
                    lst.append(matrix[n_rows-1][j]) 
                direction = 'up'
                matrix = matrix[:-1]
            elif direction == 'up' : 
                for j in range(n_rows-1,-1,-1):
                    lst.append(matrix[j][0]) 
                direction = 'right'
                matrix = list(map(lambda x : x[1:],matrix))
            if matrix !=[] and len(matrix[0]):
                n_rows, n_cols = len(matrix), len(matrix[0])  
            else : 
                flag = False
        return lst
