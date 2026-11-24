from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []

        def helper(i):
            if i == len(nums):
                candidate = sorted(curr)  # Always sort before checking or storing
                if candidate not in res:  # Now comparing sorted vs sorted
                    res.append(candidate)
                return

            curr.append(nums[i])
            helper(i + 1)
            curr.pop()
            helper(i + 1)

        helper(0)
        return res