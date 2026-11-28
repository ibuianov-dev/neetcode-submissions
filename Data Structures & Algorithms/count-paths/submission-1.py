class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        rows, cols = n, m
        paths_grid = [[0] * cols for _ in range(rows)]

        for col in range(cols):
            paths_grid[0][col] = 1
        for row in range(rows):
            paths_grid[row][0] = 1

        for row in range(1, rows):
            for col in range(1, cols):
                paths_grid[row][col] = paths_grid[row - 1][col] + paths_grid[row][col - 1]
        
        return paths_grid[-1][-1]
