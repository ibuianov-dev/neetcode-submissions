class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        islands_count = 0
        
        def bfs(r, c):
            queue = deque([(r, c)])
            grid[r][c] = '0'
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            while queue:
                row, col = queue.popleft()

                for row_offset, col_offset in directions:
                    new_row, new_col = row + row_offset, col + col_offset

                    if (new_row < 0 or new_row >= ROWS) or (new_col < 0 or new_col >= COLS):
                        continue
                    if grid[new_row][new_col] == '1':
                        grid[new_row][new_col] = '0'
                        queue.append((new_row, new_col))
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1':
                    islands_count += 1
                    bfs(r, c)

        return islands_count