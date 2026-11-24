class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        rows, cols = len(grid), len(grid[0])
        
        def dfs(r, c):
            # Base case: out of bounds or water
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
                return 0
            # Mark as visited
            grid[r][c] = 0
            # Explore neighbors + count current cell
            return 1 + dfs(r+1, c) + dfs(r-1, c) + dfs(r, c+1) + dfs(r, c-1)
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    area = dfs(i, j)
                    max_area = max(max_area, area)
        
        return max_area

        '''
        U-> Understand
        M-> Map
        P-> Plan
        I-> Implemen
        R-> Review
        E-> Evaluate




        '''
        


        