class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        count = [0]
        def dfs(i, j):
            if i >= len(grid) or i<0 or j<0 or j >= len(grid[0]):
                return 
            if grid[i][j] == 0:
                return 
            print("i",i)
            print("j",j)
            grid[i][j] = 0
            count[0] += 1
            print(count[0])

            dfs(i+1, j)
            dfs(i, j+1)
            dfs(i-1, j)
            dfs(i, j-1)

        print(count[0])



        new_count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                dfs(i, j)
                if count[0] > new_count:
                    new_count = count[0]
                
                count[0] = 0
                print(count[0])
        print(new_count)
        return new_count
        