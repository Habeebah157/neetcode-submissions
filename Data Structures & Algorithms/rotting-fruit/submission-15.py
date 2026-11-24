class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # ❌ Remove the bad early return
        # if grid and grid[0] and grid[0][0] == 0:
        #     return 0
        
        affected = deque()
        time = -1  # will become 0 after first level (initial rotten), even if no propagation

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
        
        # Check for any remaining fresh oranges
        for r in range(len(grid)):
            for c in range(len(grid[0])): 
                if grid[r][c] == 1: 
                    return -1

        # ✅ Fix: if no oranges were rotten initially, time stays -1 → but if no fresh, answer is 0
        return time if time != -1 else 0