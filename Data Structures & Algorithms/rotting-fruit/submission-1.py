class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        q = collections.deque()
        time = 0
        ROWS = len(grid)
        COLUMNS = len(grid[0])
        FRESH = 1
        ROTTEN = 2
        for i in range(ROWS): 
            for j in range(COLUMNS): 
                if grid[i][j] == FRESH: 
                    fresh += 1
                if grid[i][j] == ROTTEN: 
                    q.append((i, j))
        
        while q and fresh > 0: 
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            lenght = len(q)
            for i in range(lenght):
                x, y = q.popleft()
                
                
                for i, j in directions: 
                    row, column = i+x, j+y
                    if (row in range(ROWS)
                        and column in range(COLUMNS)
                        and grid[row][column] == 1): 
                        grid[row][column] = 2
                        q.append((row, column))
                        fresh-=1
            time+=1
        return time if fresh == 0 else -1
                


        

    