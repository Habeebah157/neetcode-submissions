class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maximum = 0  
        def rec(x, y):
            if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or grid[x][y] == 0:
                return 0
            grid[x][y] = 0
            return 1 + rec(x+1, y) + rec(x-1, y) + rec(x, y+1) + rec(x, y-1)
        
        for x in range(len(grid)): 
            for y in range(len(grid[0])): 
                if grid[x][y] == 1: 
                    maximum = max(rec(x, y), maximum)
        
        return maximum