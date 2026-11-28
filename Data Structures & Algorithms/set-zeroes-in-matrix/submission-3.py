class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])
        is_first_row_zero = False
        is_first_col_zero = False

        for col in range(COLS):
            if matrix[0][col] == 0:
                is_first_row_zero = True
        
        for row in range(ROWS):
            if matrix[row][0] == 0:
                is_first_col_zero = True

        for row in range(1, ROWS):
            for col in range(1, COLS):
                if matrix[row][col] == 0:
                    matrix[row][0] = 0
                    matrix[0][col] = 0

        for row in range(1, ROWS):
            for col in range(1, COLS):
                if matrix[0][col] == 0 or matrix[row][0] == 0:
                    matrix[row][col] = 0

        if is_first_row_zero:
            for col in range(COLS):
                matrix[0][col] = 0

        if is_first_col_zero:
            for row in range(ROWS):
                matrix[row][0] = 0
                