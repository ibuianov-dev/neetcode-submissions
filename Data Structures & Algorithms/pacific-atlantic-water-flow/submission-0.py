class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pacific_reach = set()
        atlantic_reach = set()
        result = []

        def dfs(r, c, last_val, ocean_set):
            if (r < 0 or r >= ROWS) or (c < 0 or c >= COLS):
                return
            if (r, c) in ocean_set:
                return

            if last_val <= heights[r][c]:
                ocean_set.add((r, c))
                dfs(r + 1, c, heights[r][c], ocean_set)
                dfs(r - 1, c, heights[r][c], ocean_set)
                dfs(r, c + 1, heights[r][c], ocean_set)
                dfs(r, c - 1, heights[r][c], ocean_set)

        for c in range(COLS):
            dfs(0, c, heights[0][c], pacific_reach)
        for r in range(ROWS):
            dfs(r, 0, heights[r][0], pacific_reach)

        for c in range(COLS):
            dfs(ROWS - 1, c, heights[-1][c], atlantic_reach)
        for r in range(ROWS):
            dfs(r, COLS - 1, heights[r][-1], atlantic_reach)

        for cell in pacific_reach:
            if cell in atlantic_reach:
                result.append([cell[0], cell[1]])

        return result

            