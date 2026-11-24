from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        curr = []
        res = []
        
        def dfs():
            if len(curr) == len(nums):  # Base case: permutation complete
                res.append(curr.copy())
                return
            
            for i in range(len(nums)):
                if nums[i] in curr:
                    continue
                curr.append(nums[i])
                dfs()         # Don't pass index — we're not using it meaningfully
                curr.pop()
        
        dfs()
        return res