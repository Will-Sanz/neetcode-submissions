class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        first_row, first_col = False, False
        for r in range(0, len(matrix)):
            if matrix[r][0] == 0:
                first_col = True
        for c in range(0, len(matrix[0])):
            if matrix[0][c] == 0:
                first_row = True
        
        for r in range(1, len(matrix)):
            for c in range(1, len(matrix[0])):
                if matrix[r][c] == 0:
                    matrix[r][0], matrix[0][c] = 0, 0
        
        for r in range(1, len(matrix)):
            for c in range(1, len(matrix[0])):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0
        
        if first_row:
            for c in range(len(matrix[0])):
                matrix[0][c] = 0
        if first_col:
            for r in range(len(matrix)):
                matrix[r][0] = 0
        
        
        
        