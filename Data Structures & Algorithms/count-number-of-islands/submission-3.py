class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def dfs(x, y): 
            if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or grid[x][y] == "0":
                return 

            grid[x][y] = "0"
            dfs(x+1, y)
            dfs(x, y+1)
            dfs(x-1, y)
            dfs(x, y-1)
        res = 0

        for x in range(len(grid)): 
            for y in range(len(grid[0])): 
                if grid[x][y] == "1": 
                    dfs(x, y)
                    res+=1
        return res