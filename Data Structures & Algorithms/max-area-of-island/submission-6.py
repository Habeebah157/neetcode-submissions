class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        max_area = 0

        def dfs(x, y):
            # Boundary check and land/water check
            if x < 0 or x >= ROWS or y < 0 or y >= COLS or grid[x][y] == 0:
                return 0

            # Mark as visited by setting to 0 (sink the island)
            grid[x][y] = 0

            # Explore 4 directions and accumulate area
            return (1 + dfs(x + 1, y)
                      + dfs(x - 1, y)
                      + dfs(x, y + 1)
                      + dfs(x, y - 1))

        # Iterate through every cell
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    area = dfs(i, j)
                    max_area = max(max_area, area)

        return max_area