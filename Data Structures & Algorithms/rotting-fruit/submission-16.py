class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        affected = deque()
        time = -1 

        for r in range(len(grid)): 
            for c in range(len(grid[0])): 
                if grid[r][c] == 2: 
                    affected.append((r, c))

        def isAffected(r, c): 
            if r >= len(grid) or r < 0 or c < 0 or c >= len(grid[0]) or grid[r][c] != 1: 
                return
            affected.append((r, c))
            grid[r][c] = 2

        while affected: 
            for _ in range(len(affected)): 
                r, c = affected.popleft()
                isAffected(r+1, c)
                isAffected(r-1, c)
                isAffected(r, c+1)
                isAffected(r, c-1)
            time += 1
        

        for r in range(len(grid)):
            for c in range(len(grid[0])): 
                if grid[r][c] == 1: 
                    return -1

        return time if time != -1 else 0