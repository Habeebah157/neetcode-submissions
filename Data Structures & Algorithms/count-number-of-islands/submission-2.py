class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0

        ROWS, COLS = len(grid), len(grid[0])
        def dfs(x, y):
            if  x < 0 or x >= ROWS or y >= COLS or y < 0 or grid[x][y] == "0": 
                return 

            grid[x][y] = "0"

            dfs(x+1, y)
            dfs(x-1, y)
            dfs(x, y+1)
            dfs(x, y-1)

        for i in range(ROWS): 
            for j in range(COLS): 
                if grid[i][j] == "1":
                    dfs(i, j)
                    res+= 1

        return res

        