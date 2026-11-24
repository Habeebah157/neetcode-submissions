class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:


        sol = []
        curr = []
        candidates.sort()

        def dfs(index): 
            if sum(curr) == target: 
                if curr.copy() not in sol: 
                    sol.append(curr.copy())
                return 

            if index == len(candidates) or sum(curr) > target:  # ✅ == not =
                return
            print(index)

            curr.append(candidates[index])
            dfs(index + 1)
            curr.pop()
            dfs(index + 1)

        dfs(0)
        return sol
            

        